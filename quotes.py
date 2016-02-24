#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
# quote.py - A Random Quote Generator                                         #
# Picks a random actual quote or a fact from a database, chooses 1-3 words	  #
# and randomly switches them to new ones. Uses a natural language toolkit	  #
# module (nltk) to tag words into classes in order to choose a right type	  #
# of words to be replaced. 													  #
#                                                                             #
# Can also be used to work with song lyrics: the script reads lyrics line     #
# by line, randomizes them and outputs the result.                            #
#                                                                             #
# Uses a database (quotes.db) to store and read quotes. The database consists #
# of 3 tables:                                                                #
#   *quotes: pairs of quotes and authors taken from real people, movies and   #
#     games                                                                   #
#   *lyrics: full lyrics to songs                                             #
#   *dictionary: a table of words parsed from the other tables.               #
#                                                                             #
#                                                                             #
# Requires:                                                                   #
#  Modules                                                                    #
#  * Natural Language Toolkit                                                 #
#      http://www.nltk.org/index.html                                         #
#  * Twython:                                                                 #
#      https://twython.readthedocs.org/en/latest/                             #
#  Keys:                                                                      #
#  * The Twitter bot feature requires access tokens and keys from Twitter     #
#      https://dev.twitter.com/oauth/overview/application-owner-access-tokens #        
#                                                                             #					
#																			  #
# Change log:																  #
# 23.2.2016																	  #
#	* removed the cumbersom START, END marking of quotes.sql. Running		  #
#	  update_db() now drops and re-inserts all previous data.				  #
#	* cleaned up database creation to one function				 			  #
#	* added parse_for_dictionary() as a dedicated function for parsing		  #
#	  strings for valid words to add to the dictionary.   					  #
#	  Words with apostrophes and one letter words are not considered valid.   #
#	* additionally changed find_invalid() to reflect the above changes:		  #
#	  now also finds and deletes all one letter words     					  #
#	  and optionally deletes words with apostrophes. 		  				  #
# 4.1.2016                                                                    #
#	* changed switch() to work with capitalized words.			 		  	  #
# 27.10.2015																  #
#	* initial version 												  		  #
###############################################################################

import sqlite3 as lite
import sys
import getopt
import twython
import json
import os.path
import argparse
import nltk
import random

# Define applicable nltk tags for identifying valid words for switching.
# Run this script with --tags switch to see descriptipns of all tags.
CLASSES = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "VB", "VBN", "VBD", "VBG", "VBP", "VBZ" ]


#==============================================================================
# Database functions #
#====================#


def update_db(quick=False):
	"""Execute the contents of quotes.sql to update the database.
	This function drops and refills the quotes and lyrics tables.
	See quotes.sql for DROP TABLE commands.
	This does not touch the dictionary table.
	Arg:
		quick (boolean): whether to parse quotes and lyrics for dictionary
	"""
	con = lite.connect("quotes.db")
	cur = con.cursor()

	with con:
		print "Executing quotes.sql, please wait..."
		with open("quotes.sql") as f:
			lines = [line.rstrip("\n;").lstrip("\t") for line in f]
			for sql in lines:
				cur.execute(sql)
		print "Done"

	# check whether to parse quotes and lyrics for dictionary
	if not quick:
		print "Updating dictionary..."
		cur.execute("SELECT quote FROM quotes")
		rows = cur.fetchall()
		for row in rows:
			parse_for_dictionary(row[0])

	# finally, show info on database size
	database_size()
	print "Run 'python quote.py --tags' to see description of all tags"


def parse_for_dictionary(s, verbose=False):
	"""Parse given string for database dictionary.
	Exclude punctuation and words containing apostrophes (',`,´,’).
	Args:
		s (string): the string to parse
		verbose (boolean): whether to show which words were rejected as punctuation
	Return:
		list of words of s rejected from inserting into the dictionary
	"""
	con = lite.connect("quotes.db")
	cur = con.cursor()

	# replace occurances of ' for easier handling: nltk will tokenize words with ' as two tokens: let's -> [let, 's] 
	s = s.replace("'", "`")
	tokens = nltk.word_tokenize(s)
	punctuation = ["-", "%", "`", u"´", u"’"]
	# find tokens not having punctuation
	valid = [token for token in tokens if (not any([p in token for p in punctuation]) and len(token) > 1)]
	tagged = nltk.pos_tag([word.lower() for word in valid])

	rejected = [word for word in tokens if word not in valid]
	if verbose:
		print "Words rejected:"
		print rejected

	# store in database
	with con:
		for word, tag in tagged:
			if tag in CLASSES:
				cur.execute("SELECT * FROM dictionary WHERE word = ? AND class = ?", (word, tag))
				row = cur.fetchone()
				if row is None:		# word, tag pair is not yet in dictionary -> add it
					cur.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))

	return rejected


def get_quote():
	"""Fetch a random quote from the database.
	Return:
		(quote, author) tuple
	"""
	con = lite.connect("quotes.db")
	cur = con.cursor()

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
	con = lite.connect("quotes.db")
	cur = con.cursor()

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
		else:
			next_idx = row_idx + 1
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (next_idx, 1))
			return (title, lyric)


def get_fact():
	"""Randomize a fact and print it on screen."""
	con = lite.connect("quotes.db")
	cur = con.cursor()

	with con:
		cur.execute("SELECT * FROM quotes WHERE author=? ORDER BY RANDOM() LIMIT 1", ("fact",))
		fact = cur.fetchone()
		cur.execute("UPDATE lyrics SET status=? WHERE status=?", (3, 2))
		randomized = randomize(fact)  # print from inside this function
		

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
	con = lite.connect("quotes.db")
	cur = con.cursor()

	# tokenize, reattach apostrophes and pos tag tokens
	tokens = nltk.word_tokenize(string)
	tokens = normalize_tokens(tokens)
	tagged = nltk.pos_tag(tokens)
	
	# initialize a dict for counting the number of applicable words for switching
	tags = {tag: 0 for tag in CLASSES}

	# count the number of applicable words
	for word, tag in tagged:
		if tag in CLASSES:
			tags[tag] += 1

	# total number of words applicable for the switch
	total = sum(tags.values())

	# if the quote doesn't contain any valid words, exit with error code
	if total == 0:
		raise ValueError("Error: no valid words to change.\n" + string)

	# set the number of words to change:
	# short quote -> always change one word.
	elif total < 4:
		change_degree = 1
	
	# > 3 valid words:
	# randomize the number of words to change:
	# 1 should be much more common than 3
	else:
		dice = random.random()
		if dice <= 0.66:
			change_degree = 1
		elif dice <= 0.93:
			change_degree = 2
		else:
			change_degree = 3

	# get the tags that are actually present in the string and shuffle them
	keys = [tag for tag in tags.keys() if tags[tag] > 0]
	random.shuffle(keys)

	change_tags = []
	# randomly choose change_degree different tags to determine which words
	# to switch 
	for i in range(change_degree):
		change_tags.append(random.choice(keys))
	
	# get all words whose tags are in the list of tags to be used for the switch
	valid_words = [(word, tag) for word, tag in tagged if tag in change_tags]
	#if not valid_words:   # should not occur!
	#	raise ValueError("No valid words to change.\n" + string)

	# shuffle the list and finally choose the first change_degree words to be the
	# ones to change.
	random.shuffle(valid_words)
	words_to_change = valid_words[0:change_degree]

	old = ""
	for item in words_to_change:
		old += item[0] + " "
	print "words to replace:", old

	# get random new words from the dictionary (making sure the new tags are the same as
	# the old ones)
	# Note: there needs to enough words with the correct tags in the database for this to work.
	new_words = []
	with con:
		for word, tag in words_to_change:
			cur.execute("SELECT word, class FROM dictionary WHERE class = ? AND word != ? ORDER BY RANDOM()", (tag, word))
			db_word = cur.fetchone()

			new = db_word[0]
			# capitalize the new word if necessary:
			# whole word
			if word == word.upper():
				new = db_word[0].upper()

			# first letter only
			elif word == word.capitalize():
				new = db_word[0].capitalize()

			db_word = (new, db_word[1])
			new_words.append(db_word)
		
	new = ""
	for item in new_words:
		new = new + item[0] + " "
	print "new words:", new

	# perform the switch
	# note: the index of words_to_change matches new_words
	for idx in range(len(words_to_change)):
		change_idx = tokens.index(words_to_change[idx][0])
		tokens[change_idx] = new_words[idx][0]

	# nltk.word_tokenize interprets punctuation marks as their own tokens,
	# reattach them to previous words
	punctuation_marks = [".", ",", "!", "?", "$", ":", ";", "..."]
	for idx, token in enumerate(tokens):
		if token in punctuation_marks:
			tokens[idx-1] += token

	# filter out the now lone punctuation mark and sticht the remaining
	# tokens back to a string
	tokens = [token for token in tokens if token not in punctuation_marks]
	encoded = [(word.encode("utf-8")) for word in tokens]
	s = " ".join(encoded)

	return {"randomized": s, "new": new, "old": old}


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
	"""# Fetch a lyric and use switch() to randomize it."""
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

def database_size():
	"""Print information on the size of the database.
	Used with --size switch"""
	con = lite.connect("quotes.db")
	cur = con.cursor()

	with con:
		cur.execute("SELECT COUNT(quote) FROM quotes")
		size = cur.fetchone()
		print size[0], "quotes"

		cur.execute("SELECT COUNT(*) FROM dictionary")
		size = cur.fetchone()
		print size[0], "words"

		for item in CLASSES:
			cur.execute("SELECT COUNT(word) FROM dictionary WHERE class = ?", (item,))
			size = cur.fetchone()
			print item, size[0]


def normalize_tokens(tokens):
	"""nltk.word_tokenize() will tokenize words using ' as an apostrophe into
	two tokens: eg. "can't" -> ["can", "'t"].
	While parse_for_dictionary() will take care of not including apostophes into
	the dictionary, quotes.sql still uses ' as an apostrophe and its contents
	need to inserted into the database.
	This function normalizes tokens by reattaching the parts back together.
	Arg:
		tokens (list):  a tokenized list of a quote
	Return:
		a list of the normalized tokens
	"""
	for idx, token in enumerate(tokens):
		if "'" in token:
			tokens[idx-1] += tokens[idx]
			tokens[idx] = "DEL"

	normalized = [token for token in tokens if token != "DEL"]
	return normalized


def find_invalid():
	"""Find
	  1 database quotes which do not contain any valid tags for switching,
	  2 words in dictionary containing apostrophes, and
	  3 one letter dictionary words.
	"""
	con = lite.connect("quotes.db")
	cur = con.cursor()
	invalids = []
	
	with con:
		for row in cur.execute("SELECT quote FROM quotes"):
			quote = row[0]
			invalid = True
			tokens = nltk.word_tokenize(quote)
			tokens = normalize_tokens(tokens)
			tagged = nltk.pos_tag(tokens)

			for word, tag in tagged:
				if tag in CLASSES:
					invalid = False
					break

			if invalid:
				invalids.append(tagged)

		if invalids:
			print "Invalid quotes:"
			for item in invalids:
				print item
		else:
			print "No invalid quotes."

		# check dictionary for apostrophes
		# is this really the way to go?
		cur.execute("SELECT * FROM dictionary WHERE word LIKE ? OR word LIKE ? OR word LIKE ? OR word LIKE ? OR word LIKE ?", (u"%'%", u"%`%", u"%´%", u'%"%', u"%’%"))
		invalids = cur.fetchall()
		if invalids:
			print "Words with apostrophes (', ´, `, ’):"
			print invalids

			# ask for deletion
			delete = raw_input("Remove these from database? (y/N)\n")
			if delete == "y":
				cur.execute("DELETE FROM dictionary WHERE word LIKE ? OR word LIKE ? OR word LIKE ? OR word LIKE ? OR word LIKE ?", (u"%'%", u"%`%", u"%´%", u'%"%', u"%’%"))
				print str(len(invalids)) + " entries deleted."
			else:
				print "No deletions done."
		else:
			print "No words with apostrophes."

		# check for one letter words
		cur.execute("SELECT word FROM dictionary WHERE length(word) = ?", (1,))
		invalid = cur.fetchall()
		if invalid:
			cur.execute("DELETE FROM dictionary WHERE length(word) = ?", (1,))
			print "Deleted the following one letter words:"
			print invalid
		

#==============================================================================
# Main #
#======#

def main():
	parser = argparse.ArgumentParser(description="A quote randomizer.")
	parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
	parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
	parser.add_argument("--rebuild-database", nargs="?", metavar="mode", const="full", help="Rebuilds the entire database by executing quotes.sql. Drops all previous data from quotes and lyrics but does not modify the dictionary. If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary. If mode is set to 'quick' the dictionary is not modified.")
	parser.add_argument("--song", help="Generates the next song lyric from the database or nothing if the current song is finished. To start the next song generate at least one regular quote.", action="store_true")
	parser.add_argument("--init-song", help="Changes the status codes for the lyrics table back to initial values.", action="store_true")
	parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by the '--song' switch. See the search column of the lyrics table for valid names.")
	parser.add_argument("--find-duplicates", help="Prints the first instance of quotes having a duplicate in the database.", action="store_true")
	parser.add_argument("--find-invalid", help="Find all quotes that do not contain proper words to change. Also searches the dictionary for single letter words and words containing apostrophes and prompts for deletion.", action="store_true")
	parser.add_argument("--bot", metavar="mode", help="Generates a quote or a song lyric and posts it to Twitter. Mode should be either 'quote' or 'song'. Requires access tokens and API keys from Twitter.")
	parser.add_argument("--fact", help="Generate a randomized fact", action="store_true")

	args = parser.parse_args()
	#print args

	# no database detected -> create it, show usage information and exit
	if not os.path.isfile("quotes.db"):
		ans = raw_input("The database quotes.db does not exist. Create a new one? (y/N)\n")
		if ans == "y":
			with lite.connect("quotes.db"):
				cur.execute("CREATE TABLE dictionary (word TEXT, class TEXT)")
			update_db()
			print "usage:"
			parser.print_help()
			sys.exit()


	con = lite.connect("quotes.db")
	cur = con.cursor()

	if args.size:
		database_size()

	elif args.tags:
		nltk.help.upenn_tagset()

	# rebuild database. If no optional parameter was provided, also recreate the dictionary.
	elif args.rebuild_database:
		quick = False
		mode = args.rebuild_database # check for optional parameter, if none default to 'full'

		if mode not in ["full", "quick"]:
			print "Error: invalid mode, please use either 'full' (default) or 'quick'."
			sys.exit()

		if mode == "quick":
			quick = True
		update_db(quick)

	elif args.song:
		randomize_lyric()

	# change the status codes of the lyrics table back to initial values
	elif args.init_song:
		with con:
			# set all end-of-song codes back to 1
			cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
			# set the row index back to the first row of the first song
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, 1))
		print "Done"

	# attempt to set the provided song to be the next one read from the database
	elif args.set_song:
		arg = args.set_song
		with con:
			cur.execute("SELECT rowid FROM lyrics WHERE search = ?", (arg,))
			row = cur.fetchone()

			if row == None:
				print "Invalid song"
				sys.exit(1)
			else:
				cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
				cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (row[0], 1))

	elif args.find_duplicates:
		with con:
			query = "SELECT rowid, quote FROM quotes GROUP BY quote HAVING COUNT(*) > 1"
			for dupe in cur.execute(query):
				print dupe[0], dupe[1]

	elif args.find_invalid:
		print "Checking database for invalid entries, please wait."
		find_invalid()

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
				msg = "Random non-fact:\n"+randomized_lyric[0]
			else:
				msg = randomized_quote[0]+"\n"+"--"+randomized_quote[1]

		else: 	# mode == "song"
			randomized_lyric = randomize_lyric()
			title = randomized_lyric[0]
			lyric = randomized_lyric[1]
			if title != None:
				msg = randomized_lyric[0]+'\n'+randomized_lyric[1]
			else:
				msg = randomized_lyric[1]


		with open("keys.json") as f:
			data = json.load(f)
			API_KEY = data["API_KEY"]
			API_SECRET = data["API_SECRET"]
			OAUTH_TOKEN = data["OAUTH_TOKEN"]
			OAUTH_SECRET = data["OAUTH_SECRET"]

		twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
		twitter.update_status(status=msg)

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
	

	




