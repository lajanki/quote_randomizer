#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A library module for creating and adding new items to the base databases for the randomizers.
"""

import sqlite3 as lite
import collections
import random

import nltk
from nltk.corpus import brown


class Controller(object):

    def __init__(self):
        self.con = lite.connect("./quotes.db")
        self.cur = self.con.cursor()

    def create_quote_database(self):
        """Drop all current data from quotes.db and refill it from quotes.sql. Raises
        IntegrityError if either table already exists.
        """
        with self.con:
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

    def get_random_word(self, key):
        """Given a ;-delimited POS tag key, SELECT and return a random word from
        the pos_map table matching the key. The row matching the key is also
        ;-delimited. The row is split and a random word is returned.
        """
        with self.con:
            self.cur.execute(
                "SELECT match_word FROM pos_map WHERE pos_id = ? ORDER BY RANDOM() LIMIT 1", (key,))
            row = self.cur.fetchone()

        if not row:
            raise KeyError("Invalid key: {}".format(key))

        rand_word = random.choice(row[0].split(";"))
        return rand_word

    def create_pos_map(self):
        """Create a hash table of consecutive POS tags and matching words from
        an nltk corpus.
        """
        index = collections.defaultdict(set)
        brown_tagged_sents = brown.tagged_sents(categories="news", tagset="universal")

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
        with open("./quotes.txt") as f:
            lines = f.readlines()

        # strip comments, empty lines and authors
        lines = [line.rstrip("\n").split(";")
                 for line in lines if line != "\n" and not line.startswith("--")]

        return lines

    def get_size(self):
        """Print information on the size of the database.
        Used with --size switch.
        """
        with self.con:
            self.cur.execute("SELECT COUNT(quote) FROM quotes")
            size = self.cur.fetchone()
            print("quotes:", size[0])

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

        return {"dupes": dupes, "long": long_, "malformed": malformed}
