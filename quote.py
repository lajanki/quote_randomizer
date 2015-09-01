#!/usr/bin/python
# -*- coding: utf-8 -*-


###############################################################################
# quote.py - A Random Quote Generator                                         #
# Picks a random actual quote from a database, chooses 1-3 words and randomly #
# switches them to new ones. Uses a natural language toolkit module to tag    #
# words into classes in order to choose a right type of words to be replaced. #
#                                                                             #
# Can also be used to work with song lyrics: the script reads lyrics line     #
# by line, randomizes them and outputs the result.                            #
#                                                                             #
# Uses a database (quotes.db) to store and read quotes. The database consists #
# of 3 tables:                                                                #
#   quotes: pairs of quotes and authors taken from real people, movies and    #
#     games                                                                   #
#   lyrics: full lyrics to songs                                              #
#   dictionary: a table of words parsed from the other tables.                #
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
# Lauri Ajanki 31.8.2015                                                      #
###############################################################################

import sqlite3 as lite
import sys
import getopt
import twython
import json
import os.path
from nltk import word_tokenize, pos_tag, help
from random import shuffle, randint, random, choice



# Applicable nltk word classes for switching word.
# Run this script with --tags switch to see descriptipns of all tags.
CLASSES = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBN", "VBD", "VBG" ]


#*****************
# Main functions *
#*****************

# Initialization function: create an empty database and call update_db() to fill it.
# Used if the script detects quotes.db file is missing.
def create_db():
	con = lite.connect("./quotes.db")
	cur = con.cursor()
	with con:
		cur.execute("CREATE TABLE dictionary (word TEXT UNIQUE, class TEXT)")
	update_db()


# Execute the contents of quotes.sql to update the database.
# This function drops and refills the quotes and lyrics tables and
# depending on the quick parameter also parses these tables for the dictionary.
def update_db(quick=False):
	con = lite.connect("./quotes.db")
	cur = con.cursor()

	print "Creating database..."
	with con:
		f = open("./quotes.sql")
		lines = [line.rstrip("\n;").lstrip("\t") for line in f]
		for sql in lines:
			cur.execute(sql)
	f.close()
	print "Database created"

	# parse quotes and lyrics tables for the dictionary, see below.
	if not quick:	# ie. quick == False
		print "Creating dictionary..."
		create_dictionary()

	# print the size of the database
	size = database_size()
	if not size:
		print "The dictionary seems to be empty. Check the dictionary creation limits in quotes.sql\
			   and run --rebuild-database again."
		sys.exit()
	print "Run 'python quote.py --tags' to see description of all tags"


# Parse quotes and lyrics table for the dictionary.
# Only the sections marked by "START" and "END" are parsed, see quotes.sql.
def create_dictionary():
	con = lite.connect("./quotes.db")
	cur = con.cursor()

	with con:
		# get the row_ids of "START" and "END" markers
		cur.execute("SELECT rowid FROM quotes WHERE quote = 'START'")
		start = cur.fetchone()[0]
		cur.execute("SELECT rowid FROM quotes WHERE quote = 'END'")
		end = cur.fetchone()[0]

		# fetch all rows between the marked section
		for row in cur.execute("SELECT quote FROM quotes WHERE rowid > ? AND rowid < ?", (start, end)):
			# use nltk.word_tokenize() to get a list of words of the fetched row
			tokens = word_tokenize(row[0].lower())
			# reattach apostrophes back to the previous word, see normalize_tokens() below.
			tokens = normalize_tokens(tokens)
			# use nltk.pos_tag() to give tags to each word in the list given by word_tokenize()
			tagged = pos_tag(tokens)

			# find adjectives, verbs and other valid words for the dictionary.
			cur2 = con.cursor()  # new cursor for executing
			for word, tag in tagged:
				if tag in CLASSES:
					try:
						cur2.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))

					# the 'word' column in dictionary is UNIQUE. skip words that are already
					# in the database. (Note that this also prevents the same word from being
					# added as a member of another class.)
					except lite.Error as e:
						pass
		
		# same for lyrics table
		cur.execute("SELECT rowid FROM lyrics WHERE title = 'START'")
		start = cur.fetchone()[0]
		cur.execute("SELECT rowid FROM lyrics WHERE title = 'END'")
		end = cur.fetchone()[0]
		
		for lyric in cur.execute("SELECT verse FROM lyrics WHERE rowid > ? AND rowid < ?", (start, end)):
			if lyric[0] != None:
				tokens = word_tokenize(lyric[0].lower())	
				tokens = normalize_tokens(tokens)		 		 												  
				tagged = pos_tag(tokens)

				cur2 = con.cursor()
				for word, tag in tagged:
					if tag in CLASSES:
						try:
							cur2.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))
						except lite.Error as e:
							pass


		# finally, remove the "START" and "END" markers from the database, (but not
		# from the .sql file)
		cur.execute("DELETE FROM quotes WHERE quote = ? OR quote = ?", ("START", "END"))
		cur.execute("DELETE FROM lyrics WHERE title = ? OR title = ?", ("START", "END"))


# Fetch a random quote from the database.
def get_quote():
	con = lite.connect("./quotes.db")
	cur = con.cursor()

	with con:
		cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
		randomized = cur.fetchone()

		# update lyrics table's status codes to allow the processing of the next song
		cur.execute("UPDATE lyrics SET status=? WHERE status=?", (3, 2))

		return (randomized[0], randomized[1]) # == (quote, author)



# Randomize a quote by calling switch().
#   quote_record: a (quote, author) tuple given by get_quote()
def randomize(quote_record):
	quote = quote_record[0]
	author = quote_record[1]

	s = switch(quote)	

	print s
	print "--"+author
	

	return (s, author)


# Perform the actual randomizing of the given string.
# Analyze the structure of the string, choose 1-3 to replace and fetch
# new words from the dictionary.
def switch(string):
	con = lite.connect("./quotes.db")
	cur = con.cursor()

	# tokenize and tag the string
	tokens = word_tokenize(string)
	tokens = normalize_tokens(tokens)
	tagged = pos_tag(tokens)
	
	# initialize a dictionary variable for counting the number of applicable words for switcinh
	tags = {tag: 0 for tag in CLASSES}

	# count the number of applicable words
	for word, tag in tagged:
		if tag in CLASSES:
			tags[tag] += 1

	# total number of valid words, used to determine the number of words to change
	total = sum(tags.values())

	# if the quote doesn't contain any valid words, exit with error code
	if total == 0:
		print "Invalid quote; nothing to parse."
		print string
		sys.exit(1)

	# set the number of words to change:
	# short quote -> always change one word.
	elif total < 4:
		change_degree = 1
	
	# the total number of valid words is > 3:
	# randomize the number of words to change.
	# make 1 be much more common than 3
	else:
		dice = random()
		if dice <= 0.66:
			change_degree = 1
		elif dice <= 0.93:
			change_degree = 2
		else:
			change_degree = 3


	# get those tags that are actually present in the string and shuffle them
	keys = [tag for tag in tags.keys() if tags[tag] > 0]
	shuffle(keys)

	change_tags = []
	# randomly choose change_degree different tags to determine which words
	# to switch 
	for i in range(change_degree):
		change_tags.append(choice(keys))
	
	# get the words whose tags are in the list of tags to be used for the switch
	valid_words = [(word, tag) for word, tag in tagged if tag in change_tags]
	if len(valid_words) == 0:
		print "No valid words to change."
		print string
		sys.exit(1)

	# shuffle the list and finally choose the first change_degree words to be the
	# ones to change.
	shuffle(valid_words)
	words_to_change = valid_words[0:change_degree]

	s = ""
	for item in words_to_change:
		s += item[0] + " "
	print "words to replace:", s

	# get random new words from the dictionary (making sure the new tags are the same as
	# the old ones)
	new_words = []
	with con:
		for word, tag in words_to_change:
			cur.execute("SELECT word, class FROM dictionary WHERE class = ? AND word != ? ORDER BY RANDOM()", (tag, word))
			new_words.append(cur.fetchone())
		
	s = ""
	for item in new_words:
		s = s + item[0] + " "
	print "new words:", s

	# make the switch
	# note: the index of the old word in words_to_change is the same as
	# that of the raplacing word in new_words
	for idx in range(len(words_to_change)):
		change_idx = tokens.index(words_to_change[idx][0])
		tokens[change_idx] = new_words[idx][0]


	# nltk.word_tokenize interprets punctuation marks as their own tokens,
	# reattach them to previous words
	punctuation_marks = [".", ",", "!", "?", "$", ":", ";", "..."]
	for idx, token in enumerate(tokens):
		if token in punctuation_marks:
			tokens[idx-1] += token	

	# filter out the lone punctuation mark
	tokens = [token for token in tokens if token not in punctuation_marks]

	# capitalize the final sentence and stich it back to a string from a list
	normalize_sentence(tokens)
	encoded = [(word.encode("utf-8")) for word in tokens]

	s = " ".join(encoded)
	return s


# Fetch the next lyric to be processed. Return None if current song is finished.
# The rowid of the next lyric to be processed is stored in the first line of the lyrics table.
def get_lyric():
	con = lite.connect("./quotes.db")
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
		# 1 - this is the last line of the current song. Change the code to 2,
		# don't return a lyric
		if status == 1:
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, row_idx))
			return (None, lyric)

		# 2 - the current song is finished, wait for permission to start the next one,
		# don't return a lyric
		elif status == 2:
			return (None, None)

		# 3 - OK to start the next one. Fetch and return the next row or None if
		# the previous song was the last one.
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

		# ei statusta: kappale kesken, päivitä ensimmäisen rivin itedot ja palauta nykyinen rivi
		# no satus code - the current song is not done. Fetch the next row and update the
		# first row.
		else:
			next_idx = row_idx + 1
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (next_idx, 1))
			return (title, lyric)

		
# Fetch lyric and use switch() to randomize it.
def randomize_lyric():
	lyric_record = get_lyric()
	title = lyric_record[0]
	lyric = lyric_record[1]

	if lyric != None:
		randomized = switch(lyric)
		print "New lyric:", randomized
		return (title, randomized)
	else:
		print "Current song finished"
		sys.exit()



#*******************
# Helper functions *
#*******************

# Prints information on the size of the database.
# Used with --size switch
def database_size():
	con = lite.connect("./quotes.db")
	cur = con.cursor()
	total = 0

	with con:
		cur.execute("SELECT COUNT(quote) FROM quotes")
		size = cur.fetchone()
		print size[0], "quotes"

		cur.execute("SELECT COUNT(*) FROM dictionary")
		size = cur.fetchone()
		total = size
		print size[0], "words"

		for item in CLASSES:
			cur.execute("SELECT COUNT(word) FROM dictionary WHERE class = ?", (item,))
			size = cur.fetchone()
			print item, size[0]
	return total


# Shows descriptions of all tags used by nltk module (by default).
# Used with --tags switch
def show_tags():
	help.upenn_tagset()


# Checks if a word in list given by nltk.word_tokenize() should be capitalized.
def normalize_sentence(quote_tokens):
	quote_tokens[0] = quote_tokens[0].capitalize()
	
	for idx, token in enumerate(quote_tokens[0:-1]):
		if token[-1] in [".", "!", "?"]:
			quote_tokens[idx+1] = quote_tokens[idx+1].capitalize()

		if quote_tokens[idx] == "i":
			quote_tokens[idx] = "I"


# quotes.sql uses ' as an apostrophe. nltk.word_tokenize() will interpret this
# as a new token eg. "can't" is tokenized as ["can", "'t"].
# Normalize this by reattaching the parts back together.
def normalize_tokens(tokens):
	for idx, token in enumerate(tokens):
		if "'" in token:
			tokens[idx-1] += tokens[idx]
			tokens[idx] = "DEL"		# mark the latter part for deletion 

	# filter out the lone parts beginning with "'"
	normalized = [token for token in tokens if token != "DEL"]
	return normalized
		

# Testfunction for normalization.
# Not in use.
def test_normalize():
	tokens = word_tokenize("Not Penny's boat. they're lying!")
	tokens2 = word_tokenize("It's everything you've ever wanted, kid.")
	tokens3 = word_tokenize("Don't kid yourself, It can't be done!")
	print "original tokens:"
	print tokens
	print tokens2
	print tokens3
	print

	print "normalized tokens:"
	norm1 = normalize_tokens(tokens)
	norm2 = normalize_tokens(tokens2)
	norm3 = normalize_tokens(tokens3)
	print norm1
	print norm2
	print norm3
	print

	print "normalized sentences:"
	normalize_sentence(norm1)
	normalize_sentence(norm2)
	normalize_sentence(norm3)
	print norm1


# Shows info on command line parameters
def usage():
	print "Usage:\n\
Run with 'python quote.py' to generate a randomized quote.\n\
Optional parameters:\n\
  --rebuild-database \n\
\tRebuilds the entire database by executing quotes.sql. Drops previous data from quotes and lyrics and parses the sections marked by \"START\" and \"END\" for the dictionary. You need to manually edit this section to keep this script from dropping and re-inserting the same words to the dictionary everytime you use this switch (ie. when adding new quotes to the database).\n\
  --rebuild-database quick \n\
\tRebuilds the database by executing quotes.sql, but does not modify the dictionary.\n\
  --song \n\
\tGenerates the next song lyric from the database or nothing if the current song is finished. To start the next song generate at least one regular quote.\n\
  --tags \n\
\tShows info on all tags used to categorize words into classes.\n\
  --size \n\
\tShows the size of the databse. \n\
  --bot quote\n\
\tGenerates a quote and posts it to Twitter. Requires access tokens and API keys from Twitter.\n\
  --bot song \n\
\tGenerates a song lyric and posts to Twitter. Requires access tokens and API keys from Twitter.\n\
\
Maintenance commands: \n\
  --init-song \n\
\tChanges the status codes for the lyrics table back to initial values. \n\
  --set-song <name> \n\
\tSets the given song to be the next one read by the --song -switch. See the search column of the lyrics table for valid names.\n\
  --find-duplicates \n\
\tPrints the first instance of quotes having a duplicate in the database."


#********
# Main  *
#********

def main():
	# Prompt for initialization if the database does not exist.
	if not os.path.isfile("quotes.db"):
		ans = raw_input("The database quotes.db doesn't exist. Create a new one? (y/N)\n")
		if ans == "y":
			create_db()
		usage()
		sys.exit()

	try:
		opts, args = getopt.getopt(sys.argv[1:],"", ["size", "tags", "rebuild-database", "song", "init-song", "set-song=", "find-duplicates", "bot="])
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit()

	# Parse through the given command line parameters:
	# No argument - generate a random quote.
	if not opts:
		new = get_quote()
		randomize(new)
	else:
		con = lite.connect("./quotes.db")
		cur = con.cursor()
		for opt, arg in opts:
			if opt == "--size":
				database_size()
			elif opt == "--tags":
				show_tags()
			
			# Rebuilds the database by executing quotes.sql.
			elif opt == "--rebuild-database":
				quick = False
				# --rebuild-database quick: also parse quotes.sql for the dictionary
				if "quick" in args:
					quick = True
				update_db(quick)

			# Generate the next lyric.
			elif opt == "--song":
				randomize_lyric()

			# Change the status codes of lyrics table back to initial values, ie. the next
			# use of --song results in the first line of the first song in the database
			# being processed.
			elif opt == "--init-song":
				with con:
					# change the end-of-song codes back to 1
					cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
					# change the rowid-to-read-next index back to 2
					cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, 1))
				print "Done"

			# Makes the given song to be the next one processed.
			# Requires an argument.
			elif opt == "--set-song":
				with con:
					cur.execute("SELECT rowid FROM lyrics WHERE search = ?", (arg,))
					row = cur.fetchone()

					if row == None:
						print "Invalid song"
						sys.exit(1)
					else:
						cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
						cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (row[0], 1))

			# Maintenance command: find quotes with duplicates in the database.
			elif opt == "--find-duplicates":
				with con:
					query = """SELECT rowid, quote
							   FROM quotes
							   GROUP BY quote
							   HAVING COUNT(*) > 1"""
					for dupe in cur.execute(query):
						print dupe[0], dupe[1]

			# Randomize a quote or a song and post the result to Twitter using twython.
			# Requires Twitter access tokens and keys.
			elif opt == "--bot":
				msg = ""
				if arg == "quote":
					quote = get_quote()
					randomized_quote = randomize(quote)
					msg = randomized_quote[0]+"\n"+"--"+randomized_quote[1]
				elif arg == "song":
					randomized_lyric = randomize_lyric()
					title = randomized_lyric[0]
					lyric = randomized_lyric[1]
					if title != None:
						msg = randomized_lyric[0]+'\n'+randomized_lyric[1]
					else:
						msg = randomized_lyric[1]

				if msg:
					# NOTE: keys.json in empty. Fill it with your own keys.
					with open("./keys.json") as f:
						data = json.load(f)
						API_KEY = data["API_KEY"]
						API_SECRET = data["API_SECRET"]
						OAUTH_TOKEN = data["OAUTH_TOKEN"]
						OAUTH_SECRET = data["OAUTH_SECRET"]

					twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
					twitter.update_status(status=msg)
		


if __name__ == "__main__":
	main()
	#test_normalize()
	

