#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
quote.py - A Random Quote Generator
Picks an actual quote or a fact from a database, chooses 1-3 words
and randomly switches them to new ones. Uses a natural language toolkit
module (nltk) to tag words into classes in order to choose a right type
of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics from another
database line by line, randomizes them and outputs the result.
"""


import nltk
import random
import os.path
import collections

import dbcontroller


class Randomizer(object):

    # valid pos-tags for words to change
    CLASSES = [
        "JJ",
        "JJR",
        "JJS",
        "NN",
        "NNS",
        "RB",
        "RBR",
        "RBS",
        "VB",
        "VBN",
        "VBD",
        "VBG",
        "VBP",
        "VBZ"
    ]

    def __init__(self, path="./"):
        """Define database connections and a base path for data files."""
        self.path = path
        self.dbcontroller = dbcontroller.Controller()

    def generate(self):
        quote = self.get_quote()
        author = quote[1]
        tokens = self.tokenize_quote(quote[0])

        # choose a random 3-gram and switch the middle word using
        # the pos tags as key
        switch_tokens = random.choice(tokens)
        switch_tags = [token[1] for token in switch_tokens]

        replace_word = self.dbcontroller.get_random_word(switch_tags)

        # stitch the tokens back to a quote
        idx = tokens.index(switch_tokens)
        # switch_tokens is a tuole, convert to a mutable type since we want to
        # modify the middle element
        switch_tokens = list(switch_tokens)
        switch_tokens[1] = (replace_word, "")
        tokens[idx] = switch_tokens

        # Stich ngram tokens back to a string.
        # tokens is a list of 3-gram tuples
        # ie "Live free or don't!" becomes:
        #  [((Live, tag), (free, tag), (or, tag)),
        #  ((free, tag), (or, tag), (don't, tag))
        #  ((or, tag), (don't, tag), (!, tag))]
        # Since we replaced the middle word of a random 3-gram, we need to
        # pick the middle word from each 3-gram. To finish the string also pick
        # the first word from the first 3-gram and the last word from the last
        # 3-gram.
        # Using string.replace without the pos tags is simpler, but we cannot
        # exclude the possibility that the switch word (or even the switch 3-gram)
        # occurs more than once.
        words = [tokens[0][0]] + [token[1] for token in tokens] + [tokens[-1][2]]
        new_quote = " ".join([w[0] for w in words])
        new_quote = Randomizer.cleanup(new_quote)

        quote_response = collections.namedtuple(
            "QuoteResponse", ["old_quote", "author", "new_quote", "new_word"])
        randomized_quote = quote_response(
            old_quote=quote[0], author=author, new_quote=new_quote, new_word=replace_word)

        return randomized_quote

    def get_quote(self):
        return self.dbcontroller.get_quote()

    def tokenize_quote(self, quote):
        """Return a list of POS-tokenized and ngrammed quote."""
        tokens = nltk.word_tokenize(quote)
        tags = nltk.pos_tag(tokens, tagset="universal")

        ngrams = nltk.ngrams(tags, 3)
        # ngrams is a generator, return a list (quotes are short anyway)
        return list(ngrams)

    # TODO
    def get_change_degree(self, tokens):
        """Given a tokenized string, determine the number of words to change."""
        if len(tokens) < 4:
            return 1  # for short strings only change 1 word

        rand = random.random()
        if rand <= 0.65:
            change_degree = 1
        elif rand <= 0.93:
            change_degree = 2
        else:
            change_degree = 3
        return change_degree

    @staticmethod
    def normalize_tokens(tokens):
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
                print(e)

        normalized = [token for token in tokens if token != "DEL"]
        return normalized

    @staticmethod
    def cleanup(s):
        """Cleanup a string by removing extra whitespace around certain punctuation character.
        This whitespace is introduced when tokenizing a string.
        """
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
        for old, new in punctuation.items():
            s = s.replace(old, new)

        return s


class QuoteRandomizer(Randomizer):
    """Randomizer for quotes and facts."""

    def __init__(self, path="./"):
        Randomizer.__init__(self, path)

    def generate(self):
        """Choose a random quote or fact from the database and randomized it."""
        quote, author = self.get_quote()
        randomized = self.randomize_string(quote)

        return (randomized, author)

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
        """Fetch a random fact from the database.
        Return:
            (fact, "fact") tuple
        """
        with self.con:
            self.cur.execute(
                "SELECT * FROM quotes WHERE author=? ORDER BY RANDOM() LIMIT 1", ("fact",))
            fact = self.cur.fetchone()[0]

        return (fact, "fact")
