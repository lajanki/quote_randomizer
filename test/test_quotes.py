#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import nltk
import sys
import os
import sqlite3 as lite

sys.path.append("../")  # append the main script folder to sys.path to be able to import quotes from it
import quotes

# Tests for the switch and string normalization functions in quote.py


class RandomizeTestCase(unittest.TestCase):
	"""Does the randomization for quotes, facts and lyrics work properly?"""

	@classmethod
	def setUpClass(self):
		"""Create a randomizer."""
		self.randomizer = quotes.Randomizer()


	@classmethod
	def tearDownClass(self):
		del self.randomizer


	def test_quote_randomizer(self):
		"""Is the result of generating a quote a tuple?
		Mostly to check the functions don't throw errors.
		"""
		quote = self.randomizer.get_quote()
		rand = self.randomizer.randomize(quote)
		self.assertIsInstance(rand, tuple)


	def test_fact_randomizer(self):
		"""Is the result of generating a fact a tuple?"""
		fact = self.randomizer.get_fact()
		rand = self.randomizer.randomize(fact)
		self.assertIsInstance(rand, tuple)



class SwitchTestCase(unittest.TestCase):
	"""Tests regarding switch() behaviour."""

	@classmethod
	def setUpClass(self):
		"""Read the quotes from the test database."""
		con = lite.connect("./test_quotes.db")
		cur = con.cursor()
		randomizer = quotes.Randomizer() # only needed in setup

		with con:
			cur.execute("SELECT * FROM quotes")
			self.quotes = cur.fetchall()

		# drop authors and randomize the quotes
		self.orig_quotes = [q[0] for q in self.quotes]
		self.processed = [randomizer.switch(q) for q in self.orig_quotes]  # items are dicts with "randomized", "old" and "new" keys


	def test_switch_length(self):
		"""Are the lengths of the original quote and the randomized quote still the same?"""
		#orig_lengths = [len(q.split()) for q in self.orig_quotes]
		#switch_lengths = [len(q["randomized"].split()) for q in self.processed]

		# compare each length individually to keep track of which quote fails (if any)
		for i, quote in enumerate(self.orig_quotes):
			orig_quote = self.orig_quotes[i]
			switch_quote = self.processed[i]["randomized"]

			self.assertEqual(len(switch_quote.split()), len(orig_quote.split()), "The lengths of '{}' and\n'{}' are not equal.".format(orig_quote, switch_quote))


	def test_switch_amount(self):
		"""Did switch() make the correctnumber of switches?"""
		for i, quote in enumerate(self.processed):
			nswitch = len(quote["old"])  # number of words that should have been changed
			orig_split = self.orig_quotes[i].split()
			switch_split = quote["randomized"].split()

			# loop over the words of the switch quote and count number of non-equal matches to the original quote
			diffs = 0
			for j, word in enumerate(switch_split):
				if word != orig_split[j]:
					diffs += 1

			self.assertEqual(diffs, nswitch, "There should be {} changes between '{}' and '{}'".format(nswitch, self.orig_quotes[i], quote["randomized"]))



class NormalizeTestCase(unittest.TestCase):
	"""String normalization test."""

	@classmethod
	def setUpClass(self):
		"""Read the quotes from the test database."""
		con = lite.connect("./test_quotes.db")
		cur = con.cursor()
		randomizer = quotes.Randomizer()

		with con:
			cur.execute("SELECT * FROM quotes")
			self.quotes = cur.fetchall()

		# drop author and randomize the quotes
		self.orig_quotes = [q[0] for q in self.quotes]
		self.processed = [randomizer.switch(q) for q in self.orig_quotes]  # items are dicts with "randomized", "old" and "new" keys


	def test_normalization(self):
		"""Does a word start with an apostrophe (')?"""
		for quote in self.processed:
			split = quote["randomized"].split()
			has_apostrophe_starts = any([x.startswith("'") for x in split])
			self.assertFalse(has_apostrophe_starts, "Found a word starting with a ' in {}".format(quote["randomized"]))


class SongProcessTestCase(unittest.TestCase):
	"""Does repeated calls to get_next_lyric() process a song properly?"""

	@classmethod
	def setUpClass(self):
		self.randomizer = quotes.Randomizer()

	@classmethod
	def tearDownClass(self):
		del self.randomizer

	def test_song_change(self):
		"""Is the return value of get_next_lyric() a tuple of two non-empty values
		after a song change?
		"""
		self.randomizer.set_song("Californication")
		lyric = self.randomizer.get_next_lyric()
		self.assertIsInstance(lyric, tuple)
		self.assertIsNotNone(lyric[0])
		self.assertIsNotNone(lyric[1])
		

	def test_full_song_process(self):
		"""Is the return value of get_next_lyric() a tuple on the first n calls
		and None on any subsequent calls?
		"""
		self.randomizer.set_song("What a Wonderful World") # 8 lines in the database

		# First 8 calls should return a tuple
		for i in range(8):
			lyric = self.randomizer.get_next_lyric()
			self.assertIsInstance(lyric, tuple)

		# subsequent calls should be None
		for i in range(2):
			lyric = self.randomizer.get_next_lyric()
			self.assertIsNone(lyric)







if __name__ == '__main__':
	# Create a test suite and run the tests.
	# Note that this only matters when this script is run directly,
	# ie. using python -m unittest -v test_quotes will run all tests!
	suite = unittest.TestLoader().loadTestsFromTestCase(SwitchTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)
