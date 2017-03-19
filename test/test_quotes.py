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



class SwitchTestCase(unittest.TestCase):
	"""Tests regarding switch() behaviour."""

	@classmethod
	def setUpClass(self):
		"""Read the quotes from the test database."""
		con = lite.connect("./test_quotes.db")
		cur = con.cursor()

		with con:
			cur.execute("SELECT * FROM quotes")
			self.quotes = cur.fetchall()

		# drop author and randomize the quotes
		self.orig_quotes = [q[0] for q in self.quotes]
		self.processed = [quotes.switch(q) for q in self.orig_quotes]  # items are dicts with "randomized", "old" and "new" keys


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

		with con:
			cur.execute("SELECT * FROM quotes")
			self.quotes = cur.fetchall()

		# drop author and randomize the quotes
		self.orig_quotes = [q[0] for q in self.quotes]
		self.processed = [quotes.switch(q) for q in self.orig_quotes]  # items are dicts with "randomized", "old" and "new" keys


	def test_normalization(self):
		"""Does a word start with an apostrophe (')?"""
		for quote in self.processed:
			split = quote["randomized"].split()
			has_apostrophe_starts = any([x.startswith("'") for x in split])
			self.assertFalse(has_apostrophe_starts, "Found a word starting with a ' in {}".format(quote["randomized"]))



if __name__ == '__main__':
	# Create a test suite and run the tests.
	# Note that this only matters when this script is run directly,
	# ie. using python -m unittest -v test_quotes will run all tests!
	suite = unittest.TestLoader().loadTestsFromTestCase(SwitchTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)
