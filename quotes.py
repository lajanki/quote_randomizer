#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
quote.py - A Random Quote Generator
Picks a random actual quote or a fact from a database, chooses 1-3 words
and randomly switches them to new ones. Uses a natural language toolkit
module (nltk) to tag words into classes in order to choose a right type
of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics line
by line, randomizes them and outputs the result.

Uses a database (quotes.db) to store and read quotes. The database consists
of 3 tables:
  * quotes: pairs of quotes and authors taken from real people, movies and
	games
  * lyrics: full lyrics to songs
  * dictionary: a table of words parsed from the other tables.

Requires:
  Modules
	* Natural Language Toolkit
	  http://www.nltk.org/index.html
	* Twython:
	  https://twython.readthedocs.org/en/latest/
  Keys:
	* The Twitter bot feature requires access tokens and keys from Twitter
	  https://dev.twitter.com/oauth/overview/application-owner-access-tokens


TODO: a bunch of stuff:
 * check quotes.sql for apostrophe usage and include lyrics part to existing checks
 * better detection for tags to change (ngrams?)   				


Change log:
22.3.2017
  * Rewritten as a class to better handle database connections and in order to
    provide a mechanism for keeping the bot's lyrics table processing separate
    from this script.
  * Further simplified song processing: status data is now stored in a separate
    table and the old status column is now removed.
21.3.2017
  * Simplified song processing and moved using it under the bot feature in bot.py.
  * Moved the default behaviour of generating a quote under --quote switch for
    easier debugging.
17.3.2017
  * Bugfixes regarding how percentages are tokenized.
  * Added some unit tests to ./test.
  * Refactoring: moved the Twitterbot part to its own module.
10.1.2017
  * Minor changes to reflect database table creation changes in quotes.sql:
    rather than DROPPING and CREATING the quotes table when ever quotes.sql is
    executed, all dictionary tables are now created by this script if it detects
  	the database doesn't exist.
  * Renamed --rebuild-database to --update-database to better reflect the above changes.
6.1.2017
  * (word, tag) pairs in the dictionary table are now also UNIQUE. (again,
    this would have simplified things from the start...)
28.12.2016
  * Made the quote column in the database UNIQUE, this should have probably
    been there from the start. Also removed the, now redundant, redundancy check.
  * Added a frequency column to the database to indicate the number of times
    a quote was randomly picked.
  * Added a confirmation prompt for clearing the dictionary when using
  	--rebuild-database. This sure would have been useful earlier...
26.7.2016
  * Simplified switch(). Someone sure wrote a convoluted way to achieve
	a simple task.
  * Moved the database connection and cursor object to global variables
	to prevent the nested db functions from creating new ones on each
	invocation.
11.7.2016
  * Refactoring: moved general database query functions update_db(),
	parse_for_dictionary() and database_size() to their own module for
	easier access to other scripts utilizing the database.
29.3.2016
  * Changed parse_for_dictionary() to guard against all invalid dictionary
	entries, the --find-invalid switch is now depricated
23.2.2016
  * Removed the cumbersom START, END marking of quotes.sql. Running
	update_db() now drops and re-inserts all previous data.
	This is slower, but this function is rarely used.
  * Cleaned up database creation to one function
  * Added parse_for_dictionary() as a dedicated function for parsing
	strings for valid words to add to the dictionary.
	Words with apostrophes and one letter words are not considered valid.
  * Additionally changed find_invalid() to reflect the above changes:
	now also finds and deletes all one letter words
	and optionally deletes words with apostrophes.
4.1.2016
  * Changed switch() to work with capitalized words.
27.10.2015
  * Initial version.
"""



import sys
import argparse
import nltk
import random
import os.path
import sqlite3 as lite

import dbaccess


class Randomizer():


	def __init__(self, name = "main"):
		"""Define database connections.
		Arg:
			name (string): instance name, separates normal usage of database resources from
				how the bot uses them. (Mainly keeps the bot's lyrics table status
				separate from the data when running this script on it's own)
		"""
		self.path = "./"
		self.name = name

		self.con, self.cur = self.get_database_connection_or_exit(self.path + "quotes.db")

		# Add an entry to the lyrics_status table if there isn't one for the
		# provided name. 
		if name not in  ("main", "bot"):  # only access the database if name is not among known ones
			self.add_lyrics_status_entry()



	#==============================================================================
	# Database functions #
	#====================#

	def get_database_connection_or_exit(self, path):
		"""Return a (connection, cursor)-pair to the database. Prompts for creation
		if the database doesn't exist.
		"""
		if not os.path.isfile(path):
			con = lite.connect(path)
			cur = con.cursor()

			ans = raw_input("The database quotes.db does not exist. Create a new one? This may take a while (y/N)\n")
			if ans == "y":			
				with con:
					# Create the three tables and populate them in update_db() and build_dictionary().
					cur.execute("CREATE TABLE quotes (quote TEXT UNIQUE NOT NULL, author TEXT NOT NULL, frequency INTEGER DEFAULT 0)")
					cur.execute("CREATE TABLE dictionary (word TEXT, class TEXT, UNIQUE(word, class))")
					cur.execute("CREATE TABLE lyrics (title TEXT, search TEXT UNIQUE, verse TEXT)")
					cur.execute("CREATE TABLE lyrics_status (name TEXT UNIQUE, current_song TEXT, current_row INTEGER)")

				dbaccess.update_db()
				dbaccess.build_dictionary()
				parser.print_help()
				#return con, cur

			sys.exit()  # exit regarldless of whether user answer was yes or no

		# Database already exists, setup connection objects
		con = lite.connect(path)
		cur = con.cursor()
		return con, cur


	def get_quote(self):
		"""Fetch a random quote or a fact from the database.
		Return:
			(quote, author) tuple
		"""
		with self.con:
			self.cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
			row = self.cur.fetchone()

			# update the frequency column
			frequency = row[2] + 1
			quote = row[0]
			self.cur.execute("UPDATE quotes SET frequency=? WHERE quote=?", (frequency, quote))

		return (row[0], row[1])


	def get_fact(self):
		"""Return a random fact from the database."""
		with self.con:
			self.cur.execute("SELECT * FROM quotes WHERE author=? ORDER BY RANDOM() LIMIT 1", ("fact",))
			fact = self.cur.fetchone()[0]

			return (fact, "fact")


	#=================#
	# Song processing #
	#=================#

	def get_next_lyric(self):
		"""Each song in the lyrics table is meant to be processed line-by-line. This functions returns the
		next line of lyrics to be processed by switch().
		The rowid of the database row to read is stored in the status (ie. first) line of the lyrics table.
		Calls sys.exit() if the next line of lyrics is from another song.
		Return:
			A tuple of (title, lyric) the lyric read from the database or None if the previous song has
			been fully processed. The tile of a song is != None only for the first lyric of each song
				denoting a change in song.
		"""
		with self.con:
			# Read current song status from lyrics_status table.
			self.cur.execute("SELECT * FROM lyrics_status WHERE name = ?", (self.name,))
			status = self.cur.fetchone()
			current_title = status[1]
			current_row = status[2]

			if not current_title:
				print "No song set, initialize new song with python bot.py --set-song and try again."  # only bot.py has the proper switch
				return  # returns None. This is followed by sys.exit() in randmize_lyric()

			# Fetch the row to process.
			self.cur.execute("SELECT * FROM lyrics WHERE rowid = ?", (current_row,))
			data = self.cur.fetchone()

			# Was there a row to fetch?
			if not data:
				self.cur.execute("UPDATE lyrics_status SET current_song = ? WHERE name = ?", (None, self.name)) # empty current_song
				print "Current song finished, initialize a new song with python bot.py --set-song and try again."
				return

			# Row belongs to current song => return (title, lyric)-pair and increment row index in the status row.
			elif not data[0] or data[0] == current_title:
				self.cur.execute("UPDATE lyrics_status SET current_row = ? WHERE name = ?", (current_row + 1, self.name))
				return (data[0], data[2])  # title (ie. data[0]) is !None only for the first line of each song

			# Row starts a new song => clear title from the status row and prompt for a song change.
			elif data[0] != current_title:
				self.cur.execute("UPDATE lyrics_status SET current_song = ? WHERE name = ?", (None, self.name))
				print "Current song finished, initialize a new song with --set-song and try again."
				return


	def set_song(self, search_term):
		"""Set the next song to be processed by get_next_lyric().
		Arg:
			search_term (string): the song to process next, one of the values in the search
			column of the lyrics table.
		"""
		with self.con:
			self.cur.execute("SELECT rowid, title FROM lyrics WHERE search = ?", (search_term,))
			row = self.cur.fetchone()

			# Input didn't match to the table => print valid options on screen.
			if not row:
				print "Invalid option."
				valid = self.get_songs()  # opens another database connection! (is this bad?)
				print "Valid options (case sensitive):"
				for name in valid:
					print name
				
			# Update the status row with the title and start row index of the selected song.
			else:
				self.cur.execute("UPDATE lyrics_status SET current_song=?, current_row=? WHERE name=?", (row[1], row[0], self.name))
				print "Next song set to", search_term


	def get_songs(self):
		"""Return a list of valid search terms to use with --set-song."""
		with self.con:
			self.cur.execute("SELECT search FROM lyrics")
			data = self.cur.fetchall()
			return [search[0] for search in data if search[0]] # drop empty strings


	def add_lyrics_status_entry(self):
		"""Add a new entry to the lyrics_status table for self.name if
		not already present.
		"""
		with self.con:
			try: # name is UNIQUE, return if self.name is already present
				cur.execute("INSERT INTO lyrics_status(name) VALUES (?)", (self.name,))
			except lite.IntegrityError as e:
				return


	#==============================================================================
	# Randomizing functions #
	#=======================#

	def switch(self, string):
		"""Perform the actual randomizing of the given string.
		Analyze the structure of the string, replace 1-3 words with ones fetched
		from database.
		Raise:
			ValueError when the input string doesn't contain valid words to change
		Arg:
			string (string): the string to randomize
		Return:
			a dict of the randomized string, words replaced and words inserted
		"""
		# tokenize, reattach apostrophes and pos tag tokens
		tokens = Randomizer.normalize_tokens(nltk.word_tokenize(string))
		tagged = nltk.pos_tag(tokens)

		invalid_tokens = [
			"'",
			"http",
			"@",
			"//",
			"#",
			"%"
		]

		# format a list of (idx, word, tag) tuples of valid tokens in tagged
		valid = [ (idx, item[0], item[1]) for idx, item in enumerate(tagged)
			if not any(token in item[0] for token in invalid_tokens) and item[1] in dbaccess.CLASSES ]

		# determine the number of switches to make based on number of valid words detected
		if not valid:
			raise ValueError("Error: no valid words to change.\n" + string)

		elif len(valid) < 4:
			change_degree = 1

		else:
			dice = random.random()
			if dice <= 0.66:
				change_degree = 1
			elif dice <= 0.93:
				change_degree = 2
			else:
				change_degree = 3

		words_to_change = random.sample(valid, change_degree)

		# fetch new words from database and make the switch
		new_words = []
		with self.con:
			for token in words_to_change:
				self.cur.execute("SELECT word, class FROM dictionary WHERE class = ? AND word != ? ORDER BY RANDOM()", (token[2], token[1]))
				db_word = self.cur.fetchone()
				new = db_word[0]

				# capitalize the new word if necessary:
				# the whole word
				if token[1] == token[1].upper():
					new = new.upper()

				# first letter only
				elif token[1] == token[1].capitalize():
					new = new.capitalize()

				# replace the old word at tokens with this word
				tokens[token[0]] = new
				new_words.append(new)


		# join the word back together and trim extra whitespace around punctuation
		punctuation = {
			" .": ".",
			" ,": ",",
			" !": "!",
			" ?": "?",
			" :": ":",
			" ;": ";",
			" %": "%",
			"$ ": "$",
			"@ ": "@",
			"# ": "#",
			"`` ": "\"",
			"''": "\"",
			"https: ": "https:",
			"http: ": "http:"
		}
		s = " ".join(tokens)
		for old, new in punctuation.iteritems():
			s = s.replace(old, new)

		return {"randomized": s, "old": words_to_change, "new": new_words}

		
	def randomize(self, quote_record):
		"""Randomize a quote by calling switch().
		Arg:
			quote_record (tuple): a (quote, author) tuple given by get_quote()
		Return:
			a tuple of randomized quote and original author
		"""
		quote = quote_record[0]
		author = quote_record[1]

		rand = self.switch(quote)["randomized"]	
		return (rand, author)


	def randomize_lyric(self):
		"""Fetch a lyric and randomize it."""
		lyric_record = self.get_next_lyric()
		# get_next_lyric() returns None if there is nothing more to process
		if not lyric_record:
			sys.exit()


		title = lyric_record[0]
		lyric = lyric_record[1]

		randomized = self.switch(lyric)["randomized"]
		return (title, randomized)


	#==============================================================================
	# Helper functions #
	#==================#
	@classmethod
	def normalize_tokens(self, tokens):
		"""nltk.word_tokenize() will tokenize words using ' as an apostrophe into
		two tokens: eg. "can't" -> ["can", "'t"].
		This function normalizes tokens by reattaching the parts back together. This will prevent
		switch() from choosing the prefixes to be switched (words with apostrophes would be rejected anyway).
		Arg:
			tokens (list):  a tokenized list of a quote
		Return:
			a list of the normalized tokens"""
		for idx, token in enumerate(tokens):
			try:
				if "'" in token:
					tokens[idx-1] += tokens[idx]
					tokens[idx] = "DEL"
			except IndexError as e:
				print e

		normalized = [token for token in tokens if token != "DEL"]
		return normalized


	#==============================================================================
	# Main #
	#======#

	def main(self, args):
		"""Process command line arguments."""

		#===================#
		# --update-database #
		#===================#
		# If no optional parameter was provided, also recreate the dictionary.
		if args.update_database:
			quick = False
			mode = args.update_database # check for optional parameter, if none default to 'full'

			if mode not in ["full", "quick"]:
				print "Error: invalid mode, please use either 'full' (default) or 'quick'."
				sys.exit()

			if mode == "quick":
				quick = True
			if mode == "full":
				ans = raw_input("The database will be parsed for new words in the dictionary.\
				This may take some time, continue? (y/N)\n")
				if ans != "y":
					print "Exiting."
					sys.exit()
				
			dbaccess.update_db(quick)


		#=========#
		# --quote #
		#=========#
		elif args.quote:
			quote = self.get_quote()
			rand = self.randomize(quote)
			print rand[0] + "\n--" + rand[1]


		#========#
		# --fact #
		#========#
		elif args.fact:
			fact = self.get_fact()
			rand = self.randomize(fact)
			print rand[0] + "\n--" + rand[1]


		#========#
		# --song #
		#========#
		elif args.song:
			lyric = self.randomize_lyric()
			if lyric[0]:
				print lyric[0] + "\n" + lyric[1]
			else:
				print lyric[1]


		#============#
		# --set-song #
		#============#
		elif args.set_song:
			if args.set_song == "list":
				for name in self.get_songs():
					print name

			else:
				self.set_song(args.set_song)


		#======#
		# misc #
		#======#
		elif args.size:
			dbaccess.database_size()

		elif args.tags:
			nltk.help.upenn_tagset()




if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A quote randomizer.")
	parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
	parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
	parser.add_argument("--song", help="Generate the next song lyric for the current song. Use --set-song to initialize a new song.", action="store_true")
	parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by --song. Use [list] to see valid choices.")
	parser.add_argument("--update-database", nargs="?", metavar="mode", const="full", help="""Fills the database by executing quotes.sql.
		If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary.
		If mode is set to 'quick' the dictionary is not modified.""")
	parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
	parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
	args = parser.parse_args()

	app = Randomizer()
	try:
		app.main(args)
	# switch() had nothing to switch (no valid tags)
	except ValueError as e:
		print e

		
		




