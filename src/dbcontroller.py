#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A library module for creating and adding new items to the base databases for the randomizers.
"""

import sqlite3 as lite
import collections
import random
import os

import nltk
from nltk.corpus import brown



PATH_TO_SRC = os.path.abspath(os.path.dirname(__file__))
PATH_TO_DB = os.path.join(PATH_TO_SRC, "..", "quotes.db")
PATH_TO_QUOTES_TXT = os.path.join(PATH_TO_SRC, "..", "quotes.txt")

# determine the tagset to use for determining POS tags,
# see https://github.com/slavpetrov/universal-pos-tags
NLTK_TAGSET = "universal"



class Controller(object):

    def __init__(self):
        self.con = lite.connect(PATH_TO_DB)
        self.cur = self.con.cursor()

    def create_quote_database(self):
        """Creates the two tables _quotes_ and _pos_map_ for quotes and a mapping of POS
        classes and words. Drops all previous data!
        """
        with self.con:
            try:
                self.cur.execute("DROP TABLE quotes")
                self.cur.execute("DROP TABLE pos_map")
            except lite.OperationalError: # raised if tables don't exist
                pass

            self.cur.execute("CREATE TABLE quotes (quote TEXT UNIQUE, author TEXT)")
            self.cur.execute("CREATE TABLE pos_map (pos_id TEXT PRIMARY KEY, match_word TEXT)")

    def insert_quotes(self):
        """INSERT quotes from quotes.txt to the database. Skips existing quotes."""
        quote_tokens = self.parse_quotes()
        with self.con:
            # quote column is UNIQUE, skip duplicate lines.
            try:
                self.cur.executemany("INSERT INTO quotes VALUES (? ,?)", quote_tokens)
            except (lite.Warning, lite.IntegrityError):
                pass

    def insert_pos_map(self):
        """Fill pos_map table by creating the mapping and INSERTING in to the database."""
        pos_map = self.create_pos_map()
        with self.con:
            for key in pos_map:
                match_words = ";".join(pos_map[key])

                self.cur.execute("INSERT INTO pos_map VALUES (?, ?)", (key, match_words))

    def get_quote(self):
        """SELECT and return a random (quote, author) tuple from the database."""
        with self.con:
            self.cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
            row = self.cur.fetchone()

        return row

    def get_fact(self):
        """SELECT and return a random fact from the database."""
        with self.con:
            self.cur.execute(
                "SELECT * FROM quotes WHERE author='fact' ORDER BY RANDOM() LIMIT 1")
            row = self.cur.fetchone()

        return row

    def get_random_word(self, key):
        """Given a ;-delimited POS tag key, SELECT and return a random word from
        the pos_map table matching the key. The row matching the key is also
        ;-delimited. The row is split and a random word is returned.
        """
        # if key is a list, convert to ;-delimited string
        if isinstance(key, list):
            key = ";".join(key)

        with self.con:
            self.cur.execute(
                "SELECT match_word FROM pos_map WHERE pos_id = ? ORDER BY RANDOM() LIMIT 1", (key,))
            row = self.cur.fetchone()

        if not row:
            raise KeyError("Invalid key: {}".format(key))

        rand_word = random.choice(row[0].split(";"))
        return rand_word

    def create_pos_map(self):
        """Create a mapping table of 3 consecutive POS tags and matching middle words from nltk
        internal dataset. The key is a ;-delimited string of the POS tags.
        Eg. finds all verbs with NUM, VERB, PRON sequence in the dataset.
        """
        index = collections.defaultdict(set)
        brown_tagged_sents = brown.tagged_sents(categories="news", tagset=NLTK_TAGSET)

        # create 3-grams from each sentence
        for sent in brown_tagged_sents:
            ngrams = nltk.ngrams(sent, 3)

            for ngram in ngrams:
                # join the 3 POS tags from each ngram as key to the index
                key = ";".join([token[1] for token in ngram])
                word = ngram[1][0]  # middle word as the value

                index[key].add(word)

        return index

    def parse_quotes(self):
        """Fetch list of(quote, author) tuples from quotes.txt to be inserted into the database."""
        with open(PATH_TO_QUOTES_TXT) as f:
            lines = f.readlines()

        # strip comments, empty lines and authors
        lines = [line.rstrip("\n").split(";")
                 for line in lines if line != "\n" and not line.startswith("--")]

        return lines

    def validate_quotes(self):
        """Check quotes.txt for duplicates or otherwise malformed data."""
        invalid = self.find_invalid()
        critical = invalid.dupes + invalid.malformed
        if critical:
            print("""ERROR: found the following invalid entries in quotes.txt.
            Check for extra whitespace and duplicates and try again.""")
            for item in critical:
                print(item)
            raise ValueError("Invalid data in quotes.txt")

    def find_invalid(self):
        """Find various types of invalid entries in quotes.txt(and not from the database itself).
        Each quote should:
          1 be short enough to fit in a tweet
          2 be split into two aprts as quote; author
          3 be unique
        Note: finding long quotes is not entirely reliable as the randomized quote may still be too long to tweet.
        Return:
            a dict of lists for each type of invalid entries.
        """
        long_ = []
        malformed = []
        dupes = []
        seen = []

        lines = self.parse_quotes()
        for line in lines:
            # too long?
            if len(" ".join(line)) > 135:
                long_.append(line)

            # split by ; into two parts?
            if len(line) != 2:  # line is already split by ";" into a tuple
                malformed.append(line)

            # duplicates?
            quote = line[0]
            if quote in seen:
                dupes.append(quote)
            seen.append(quote)

        InvalidQuoteContainer = collections.namedtuple(
            "InvalidQuoteContainer", ["dupes", "long", "malformed"])
        return InvalidQuoteContainer(dupes=dupes, long=long_, malformed=malformed)

    def get_size(self):
        """Print information on the size of the database.
        Used with --size switch.
        """
        with self.con:
            self.cur.execute("SELECT COUNT(quote) FROM quotes")
            size = self.cur.fetchone()
            print("quotes:", size[0])