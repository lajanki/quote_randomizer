#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Picks a real quote or a fact from a database, chooses 1-3 words
and randomly switches them to new ones with matching part-os-speech tags. Natural language toolkit
library (nltk) is used to tag words into POS classes in order to choose similar words as replacements.
"""

import nltk
import random
import os.path
import collections

from src import dbcontroller
from src import utils


class Randomizer(object):
    """A base randomizer class. Splits sentances into POS tagged words analyzes the result and
    randomly switches a number of words to with matching POS tags using built-in nltk data structure.
    """ 

    def __init__(self):
        """Setup a database connector."""
        self.dbcontroller = dbcontroller.Controller()

    def generate(self, type_="all"):
        """Generate a new quote. Chooses a random actual quote from the database and a random word to replace.
        Return
            a namedtuple of old and new quote as as well as the replacing word.
        """
        #TODO: support for more than 1 replacing word
        if type_ == "fact":
            old_quote = self.get_fact()
        else:
            old_quote = self.get_quote()

        author = old_quote[1]
        tokens = utils.tokenize_normalize_and_tag(old_quote[0])

        # Choose a 3-gram to use for the switch. The middle word will be switched.
        # We need a random 3-gram where the middle word is not punctuation or contain other invalid characters.
        valid_tokens = [token for token in tokens if token[1][1] not in (".", "CUSTOM1")]
        switch_tokens = random.choice(valid_tokens)
        old_word = switch_tokens[1][0]
        switch_tags = [token[1] for token in switch_tokens]

        # randomly choose a new word from the list of matching POS tags 
        replace_word_list = self.dbcontroller.get_matching_word_list(switch_tags)
        # Ensure we're not choosing the original word. This will cause an IndexError if either
        # the original word is not in the list (pos_map is built from different data) or
        # it was only one item to choose from.
        try:
            replace_word_list.remove(old_word)
        except ValueError: 
            pass

        try:
            replace_word = random.choice(replace_word_list)
        except IndexError:
            raise IndexError("ERROR: couldn't find a replacing word")


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

        # Note: this is essentially replicating string.replace, but we want to ensure
        # replacement of the same occurance of the word as was chosen earlier.  
        words = [tokens[0][0]] + [token[1] for token in tokens] + [tokens[-1][2]]
        new_quote = " ".join([w[0] for w in words])
        new_quote = utils.cleanup_string(new_quote)

        quote_response = collections.namedtuple(
            "QuoteResponse", ["old_quote", "author", "new_quote", "new_word"])
        randomized_quote = quote_response(
            old_quote=old_quote[0], author=author, new_quote=new_quote, new_word=replace_word)

        return randomized_quote

    def get_quote(self):
        return self.dbcontroller.get_quote()

    def get_fact(self):
        return self.dbcontroller.get_fact()

    def tokenize_and_tag(self, quote):
        """Tokenize and POS-tag a quote to a a list of 3-grams."""
        tokens = nltk.word_tokenize(quote)
        tags = nltk.pos_tag(tokens, tagset=utils.NLTK_TAGSET)

        ngrams = nltk.ngrams(tags, 3)
        # ngrams is a generator, return a list (quotes are short anyway)
        return list(ngrams)

    def tokenize_normalize_and_tag(self, quote):
        """Tokenize and POS-tag a quote to a a list of 3-grams."""
        tokens = nltk.word_tokenize(quote)
        normalized_tokens = utils.normalize_tokens(tokens)
        normalized_tags = utils.pos_tag_and_normalize(normalized_tokens)

        ngrams = nltk.ngrams(normalized_tags, 3)
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

 




