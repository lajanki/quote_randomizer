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


TODO:
    * apostrophe tokenization: you're => [you, 're].
        don't split by apostrophe? Should we ignore pos tags completely?
    * change_degree + multiple switches
    * split by sentences on tokenization?
        sent_tokenize?
        don't replace punctuation
    * don't replace words with the same word

"""

import nltk
import random
import os.path
import collections

from src import dbcontroller



class Randomizer(object):
    """A base randomizer class. Splits sentances into POS tagged words analyzes the result and
    randomly switches a number of words to with matching POS tags using built-in nltk data structure.
    """ 

    def __init__(self):
        """Setup a database connector."""
        self.dbcontroller = dbcontroller.Controller()

    def generate(self, old_quote):
        """Generate a new quote. Chooses a random actual quote from the database and a random word to replace.
        Return
            a namedtuple of old and new quote as as well as the replacing word.
        """
        #TODO: support for more than 1 replacing word
        author = old_quote[1]
        tokens = self.tokenize_quote(old_quote[0])

        # choose a random 3-gram and switch the middle word using
        # the pos tags as key
        switch_tokens = random.choice(tokens)
        switch_tags = [token[1] for token in switch_tokens]

        replace_word = self.dbcontroller.get_matching_word(switch_tags)

        # find the index of the randomly selected switch token from the original tokenized quote
        idx = tokens.index(switch_tokens)  
        # switch_tokens is a tuple, convert to a mutable type since we want to modify the middle element
        switch_tokens = list(switch_tokens)
        switch_tokens[1] = (replace_word, "")  # new pos tag value is irrelevant
        tokens[idx] = switch_tokens

        # Stich ngram tokens back to a string.
        # tokens is a list of 3-gram tuples
        # eg "Live free or don't!" becomes:
        #  [((Live, tag), (free, tag), (or, tag)),
        #  ((free, tag), (or, tag), (don't, tag))
        #  ((or, tag), (don't, tag), (!, tag))]
        # In order to rebuild the string we need he middle words from each 3-gram as well as
        # the first word from the first 3-gram and the last word from the last 3-gram

        # Note: using string.replace without the pos tags is simpler, but we cannot
        # exclude the possibility that the switch word (or even the switch 3-gram)
        # occurs more than once.
        words = [tokens[0][0]] + [token[1] for token in tokens] + [tokens[-1][2]]
        new_quote = " ".join([w[0] for w in words])
        new_quote = Randomizer.cleanup(new_quote)

        quote_response = collections.namedtuple(
            "QuoteResponse", ["old_quote", "author", "new_quote", "new_word"])
        randomized_quote = quote_response(
            old_quote=old_quote[0], author=author, new_quote=new_quote, new_word=replace_word)

        return randomized_quote

    def get_quote(self):
        return self.dbcontroller.get_quote()

    def get_fact(self):
        return self.dbcontroller.get_fact()

    def tokenize_quote(self, quote):
        """Tokenize and POS-tag a quote to a a list of 3-grams."""
        tokens = nltk.word_tokenize(quote)
        tags = nltk.pos_tag(tokens, tagset=dbcontroller.NLTK_TAGSET)

        ngrams = nltk.ngrams(tags, 3)
        # ngrams is a generator, return a list (quotes are short anyway)
        return list(ngrams)

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





