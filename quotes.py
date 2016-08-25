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

Change log:
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
  * Initial version
"""


import sqlite3 as lite
import sys
import getopt
import twython
import json
import os.path
import argparse
import nltk
import random

import dbaccess


# set connection to the database as a global variable to prevent nested function calls
# from re-creating these.
# TODO: maybe change to a class? move to dbaccess?
path = "/home/pi/python/quotes/"
con = lite.connect(path+"quotes.db")
cur = con.cursor()

# Applicable nltk word classes for switching word.
# Run this script with --tags switch to see descriptipns of all tags.
CLASSES = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "VB", "VBN", "VBD", "VBG", "VBP", "VBZ" ]

#==============================================================================
# Database functions #
#====================#
def get_quote():
	"""Fetch a random quote or a fact from the database.
	Return:
		(quote, author) tuple
	"""
	with con:
		cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
		randomized = cur.fetchone()

		# update lyrics table's status codes to allow the processing of the next song
		cur.execute("UPDATE lyrics SET status=? WHERE status=?", (3, 2))

	return (randomized[0], randomized[1])


def get_lyric():
	"""Fetch the next lyric to be processed. Return None if current song is finished.
	The rowid of the next lyric to be processed is stored in the first line of the lyrics table.
	Return:
		(title, lyric) tuple of the next lyric to be processed, possible None
	"""
	with con:
		# get the rowid of the next line to be processed
		cur.execute("SELECT status FROM lyrics WHERE rowid = ?", (1,))
		row_idx = cur.fetchone()[0]
	
		# fetch the actual row
		cur.execute("SELECT title, verse, status FROM lyrics WHERE rowid = ?", (row_idx,))
		row = cur.fetchone()

		title = row[0]
		lyric = row[1]
		status = row[2]

		# read the status code from the end of the row and act accordingly:
		# 1 - this is the last line of the current song. Change the code to 2
		# and return the lyric
		if status == 1:
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, row_idx))
			return (None, lyric)

		# 2 - the current song is finished, wait for permission to start the next one,
		# don't return a lyric
		elif status == 2:
			return (None, None)

		# 3 - OK to start the next one. Fetch and return the next row or None if
		# the previous song was the last one in the database.
		# Return both the title and the first line of lyrics
		elif status == 3:
			next_idx = row_idx + 1
			cur.execute("SELECT * FROM lyrics WHERE rowid = ?", (next_idx,))
			row = cur.fetchone()
			if row == None:
				print("No new song to fetch. Reset database with --init-song -switch")
				sys.exit(0)

			title = row[0]
			lyric = row[1]

			# update the status code of the first row to match the rowid to the next
			# row to read from
			next_idx += 1
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (next_idx, 1))

			return (title, lyric)

		# no satus code - the current song is not done. Fetch the next row and update the
		# first row.
		next_idx = row_idx + 1
		cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (next_idx, 1))
		return (title, lyric)


def get_fact():
	"""Randomize a fact and print it on screen."""
	with con:
		cur.execute("SELECT * FROM quotes WHERE author=? ORDER BY RANDOM() LIMIT 1", ("fact",))
		fact = cur.fetchone()
		cur.execute("UPDATE lyrics SET status=? WHERE status=?", (3, 2))
	randomized = randomize(fact)
		

#==============================================================================
# Randomizing functions #
#=======================#

def switch(string):
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
	tokens = normalize_tokens(nltk.word_tokenize(string))
	tagged = nltk.pos_tag(tokens)

	invalid_tokens = [
		"'",
		"http",
		"@",
		"//",
		"#",
	]

	# get tuples of (idx, word, tag) of valid tokens in tagged
	valid = [ (idx, item[0], item[1]) for idx, item in enumerate(tagged)
		if not any(token in item[0] for token in invalid_tokens) and item[1] in CLASSES ]

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
	with con:
		for token in words_to_change:
			cur.execute("SELECT word, class FROM dictionary WHERE class = ? AND word != ? ORDER BY RANDOM()", (token[2], token[1]))
			db_word = cur.fetchone()
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
		"$ ": "$",
		"@ ": "@",  #for tweets, won't fix emails!
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

	
def randomize(quote_record):
	"""Randomize a quote by calling switch().
	Arg:
		quote_record (tuple): a (quote, author) tuple given by get_quote()
	Return:
		a tuple of randomized quote and original author
	"""
	quote = quote_record[0]
	author = quote_record[1]

	s = switch(quote)["randomized"]

	print s
	print "--"+author
	
	return (s, author)


def randomize_lyric():
	"""Fetch a lyric and use switch() to randomize it."""
	lyric_record = get_lyric()
	title = lyric_record[0]
	lyric = lyric_record[1]

	if lyric != None:
		randomized = switch(lyric)["randomized"]
		print "New lyric:", randomized
		return (title, randomized)
	else:
		print "Current song finished"
		sys.exit()


#==============================================================================
# Helper functions #
#==================#
def normalize_tokens(tokens):
	"""nltk.word_tokenize() will tokenize words using ' as an apostrophe into
	two tokens: eg. "can't" -> ["can", "'t"].
	This function normalizes tokens by reattaching the parts back together. This will prevent
	switch() from choosing the prefixes to be switched. Apostrophe words are rejected anyway.
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

def main():
	parser = argparse.ArgumentParser(description="A quote randomizer.")
	parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
	parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
	parser.add_argument("--rebuild-database", nargs="?", metavar="mode", const="full", help="""Rebuilds the entire database by executing quotes.sql.
		Drops all previous data from quotes and lyrics but does not modify the dictionary. If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary.
		If mode is set to 'quick' the dictionary is not modified.""")
	parser.add_argument("--song", help="Generates the next song lyric from the database or nothing if the current song is finished. To start the next song generate at least one regular quote.", action="store_true")
	parser.add_argument("--init-song", help="Changes the status codes for the lyrics table back to initial values.", action="store_true")
	parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by the '--song' switch. See the search column of the lyrics table for valid names.")
	parser.add_argument("--find-duplicates", help="Prints the first instance of quotes having a duplicate in the database.", action="store_true")
	parser.add_argument("--bot", metavar="mode", help="Generates a quote or a song lyric and posts it to Twitter. Requires access tokens and API keys from Twitter.")
	parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")

	args = parser.parse_args()
	#print args

	#######################
	# File initialization #
	#######################
	# no database detected -> create it, show usage information and exit
	if not os.path.isfile(path+"quotes.db"):
		ans = raw_input("The database quotes.db does not exist. Create a new one? (y/N)\n")
		if ans == "y":
			with con:
				cur.execute("CREATE TABLE dictionary (word TEXT, class TEXT)")
			dbaccess.update_db()
			print "usage:"
			parser.print_help()
			sys.exit()


	if args.size:
		dbaccess.database_size()

	elif args.tags:
		nltk.help.upenn_tagset()

	######################
	# --rebuild-database #
	######################
	# If no optional parameter was provided, also recreate the dictionary.
	elif args.rebuild_database:
		quick = False
		mode = args.rebuild_database # check for optional parameter, if none default to 'full'

		if mode not in ["full", "quick"]:
			print "Error: invalid mode, please use either 'full' (default) or 'quick'."
			sys.exit()

		if mode == "quick":
			quick = True
		dbaccess.update_db(quick)

	##########
	# --song #
	##########
	elif args.song:
		randomize_lyric()

	###############
	# --init-song #
	###############
	# change the status codes of the lyrics table back to initial values
	elif args.init_song:
		with con:
			# set all end-of-song codes back to 1
			cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
			# set the row index back to the first row of the first song
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, 1))
		print "Done"

	##############
	# --set-song #
	##############
	# attempt to set the provided song to be the next one read from the database
	elif args.set_song:
		with con:
			cur.execute("SELECT rowid FROM lyrics WHERE search = ?", (args.set_song,))
			row = cur.fetchone()

			if row == None:
				print "Invalid song"
				sys.exit(1)
			else:
				cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
				cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (row[0], 1))

	#####################
	# --find-duplicates #
	#####################
	elif args.find_duplicates:
		with con:
			query = "SELECT rowid, quote FROM quotes GROUP BY quote HAVING COUNT(*) > 1"
			for dupe in cur.execute(query):
				print dupe[0], dupe[1]

	#########
	# --bot #
	#########
	# tweet
	elif args.bot:
		msg = ""
		mode = args.bot
		if mode not in ["quote", "song"]:
			print "Error: invalid mode, please use either 'quote' or 'song'."
			sys.exit()

		# format the message of the tweet based on whether the database item was a quote or a fact
		if mode == "quote":
			quote = get_quote()
			randomized_quote = randomize(quote)

			if randomized_quote[1] == "fact":
				msg = "Random non-fact:\n" + randomized_quote[0]
			else:
				msg = randomized_quote[0] + "\n" + "--" + randomized_quote[1]

		else: 	# mode == "song"
			randomized_lyric = randomize_lyric()
			title = randomized_lyric[0]
			lyric = randomized_lyric[1]
			if title != None:
				msg = randomized_lyric[0]+'\n'+randomized_lyric[1]
			else:
				msg = randomized_lyric[1]


		with open(path+"keys.json") as f:
			data = json.load(f)
			API_KEY = data["API_KEY"]
			API_SECRET = data["API_SECRET"]
			OAUTH_TOKEN = data["OAUTH_TOKEN"]
			OAUTH_SECRET = data["OAUTH_SECRET"]

		twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
		twitter.update_status(status=msg)

	##########
	# --fact #
	##########
	elif args.fact:
		get_fact()

	# no command line argument provided -> print a randomized quote or a fact on screen
	else:
		new = get_quote()
		randomize(new)		# printing from inside the function



if __name__ == "__main__":
	try:
		main()
	# switch() had nothing to switch (no valid tags)
	except ValueError as e:
		print e
	
	




