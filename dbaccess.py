#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A library module for general access points to quotes.db.

changelog
10.1.2017
  * Changed the way quotes.sql is executed: no more DROP TABLE followed by CREATE TABLE.
  	when new data is inserted. This keeps the frequency data intact. The lyrics table remains unchanged.
  * Finding suplicates within quotes.sql is now handled by parsing it as a text file.
9.1.2017
  * Minor tweaks to what's considered valid words to insert into the dictionary table:
  	the only non-alphanumeric character allowed is "-". This prevents stuff like $21
  	from being inserted. Also removed such words from the database.
6.1 2017
  * Added build_dictionary() which reads a pre tagged corpus from the nltk module
    and inserts valid (word, tag) pairs to the database. The option to parse
    quotes for the dictionary is now somewhat redundant, maybe remove in the future?
  * Minor error handling changes in parse_for_dictionary() to reflect change that
    (word, tag) pairs in the dictionary table are now unique.
4.1.2017
  * Added error handling to update_db() when multiples of the same quote is encoutered.
26.7.2016
  * Added normalize_tokens() to parse_for_dictionary() to prevent 
	the "can't" -> ["ca", "n't"] behaviour of nltk.word_tokenize().
  * Added some rejection tokens to parse_for_dictionary().
11.7.2016
  * Initial version.
"""


import nltk
import sqlite3 as lite



path = "/home/pi/python/quotes/"

# Applicable nltk word classes for switching word.
# Run this script with --tags switch to see descriptipns of all tags.
CLASSES = ("JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBN", "VBD", "VBG", "VBP", "VBZ")

def update_db(quick=False):
	"""Execute the contents of quotes.sql to update the database.
	This function drops and refills the quotes and lyrics tables.
	See quotes.sql for DROP TABLE commands.
	By default, inserted quotes are also parsed for the dictionary.
	No data is dropped from the dictionary.
	Arg:
		quick (boolean): whether to parse quotes and lyrics for dictionary
	"""
	con = lite.connect(path+"quotes.db")
	cur = con.cursor()

	with con:
		print "Executing quotes.sql, please wait..."
		with open(path+"quotes.sql") as f:
			lines = [line.rstrip("\n;").lstrip("\t") for line in f]
			for sql in lines:
				# quotes column is UNIQUE. Skip duplicate lines.
				try:
					cur.execute(sql)
				except (lite.Warning, lite.IntegrityError) as e:
					pass

	dupes = find_duplicates()
	print "Done"
	if dupes:
		print "The following duplicates were detected in quotes.sql:"
		print dupes


	# Check whether to parse quotes and lyrics for the dictionary.
	if not quick:
		print "Updating dictionary..."
		cur.execute("SELECT quote FROM quotes")
		rows = cur.fetchall()
		for row in rows:
			parse_for_dictionary(row[0])

	# Finally, show info on database size.
	database_size()
	print "Run 'python quote.py --tags' to see description of all tags."


def parse_for_dictionary(s):
	"""Parse given string for database dictionary. Exclude words already in the dictionary.
	Args:
		s (string): the string to parse
	"""
	con = lite.connect(path+"quotes.db")
	cur = con.cursor()

	# Replace occurances of ' for easier handling: nltk will tokenize words with ' as two tokens: let's -> [let, 's].
	tokens = normalize_tokens(nltk.word_tokenize(s))

	# Valid tokens to insert to the database:
	#	1) may contain "-", otherwise alphanumeric
	# 	2) len > 3
	# Note: stripping words happen after tagging to ensure the correct tag is used.
	tagged = nltk.pos_tag([word.lower() for word in tokens])
	tagged = [token for token in tagged if (token[0].replace("-", "").isalnum() and len(token[0]) > 3) ]

	if not tagged:
		print "No valid tags in:"
		print s

	# Store in database.
	with con:
		for word, tag in tagged:
			if tag in CLASSES:
				try:  # the (word, tag) needs to be unique
					cur.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))
				except lite.IntegrityError as e:
					pass


def build_dictionary():
	"""Builds the dictionary table by reading the tagged data from Brown corpus from the nltk module
	and inserts that data to the database. This corpus has a total of ~ 1.1 million (word, tag) pairs
	with ~ 42 000 valid pairs to enter in the database.
	"""
	con = lite.connect(path+"quotes.db")
	cur = con.cursor()

	print "Building a dictionary from an internal dataset. This may take a while..."
	tagged = nltk.corpus.brown.tagged_words()
	# Strip multiples and words with invalid tags and characters.
	# It's sligthly faster to first remove multiples and then remove invalid.
	tagged = set(tagged)
	tagged = [token for token in tagged if ( token[1] in CLASSES and token[0].replace("-", "").isalnum() and len(token[0]) > 3 )]
	
	print "Inserting " + str(len(tagged)) + " items to the database."
	with con:
		for word, tag in tagged:
			if tag in CLASSES:
				try:
					cur.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))
				except lite.IntegrityError as e:
					pass


####################
# Helper functions #
####################

def database_size():
	"""Print information on the size of the database.
	Used with --size switch.
	"""
	con = lite.connect(path+"quotes.db")
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


def find_duplicates():
	"""Find duplicates in quotes.sql. Extracts the part after VALUES (' and before ');
	to get the actual quote.
	Return:
		a list of duplicate quotes detected.
	"""
	uniques = [];
	dupes = [];
	with open(path+"quotes.sql") as f:
		for line in f:
			if "INSERT INTO lyrics" in line:  # break when the lyrics table data is encoutered
				break
			if line == "\n" or line.startswith("--"):  # skip empty lines and comments
				continue

			# Strip the sql from the beginning and the end.
			line = line.lstrip("INSERT INTO quotes(quote, author) VALUES") # Note that this still leaves a "'" (but not a space or "("!) to the beginning...
			line = line.lstrip("'")  #...this way no actual quote characters are removed (not that this really matters, though).
			line = line.rstrip("');\n")
			# Split by ', to get the quote from the (quote, author pair)
			quote = line.split("',")[0]

			# Check if this quote has already been seen
			if quote in uniques:
				dupes.append(quote)
			else:
				uniques.append(quote)

	return dupes


def normalize_tokens(tokens):
	"""nltk.word_tokenize() will tokenize words using ' as an apostrophe into
	two tokens: eg. "can't" -> ["can", "'t"].
	This function normalizes tokens by reattaching the parts back together and
	Returns the result as a tokenized list.
	Arg:
		tokens (list):  a tokenized list of a quote
	Return:
		a list of the normalized tokens"""
	for idx, token in enumerate(tokens):
		try:
			if "'" in token:
				tokens[idx-1] += tokens[idx]
				tokens[idx] = "DEL"

		# The first token contained "'". This shouldn't occur anyway.
		except IndexError as e:
			print e

	normalized = [token for token in tokens if token != "DEL"]
	return normalized

