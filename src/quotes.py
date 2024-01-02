# Picks a real quote or a fact from a database, chooses 1-3 words
# and randomly switches them to new ones with matching part-os-speech tags. Natural language toolkit
# library (nltk) is used to tag words into POS classes in order to choose similar words as replacements.

# Currently uses the simplified, "universal tagset" (see, https://www.nltk.org/book/ch05.html
# and https://www.nltk.org/_modules/nltk/tag/mapping.html). This doesn't differentiate between verb tenses or modes
# or noun types (proper/common). Should this be changed to more fine grainde tagset such as "upenn"?


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
        if type_ == "fact":
            old_quote = self.get_fact()
        else:
            old_quote = self.get_quote()

        author = old_quote[1]
        tokens = utils.tokenize_normalize_and_tag(old_quote[0])

        # Choose a 3-gram to use for the switch. The middle word will be switched.
        # We need a random 3-gram where the middle word is not punctuation or contain other invalid characters.
        valid_tokens = [token for token in tokens if token[1][1] not in (".", "CUSTOM1")]

        change_degree = self.get_change_degree(valid_tokens)
        tokens_to_switch = random.sample(valid_tokens, change_degree)
        # Perform the switch
        new_tokens = self.switch_tokens(tokens, tokens_to_switch)

        # Stich tokenized quote back to a string.
        # Tokens is a list of 3-gram tuples, eg. "Live free or don't!" becomes:
        #  [((Live, tag), (free, tag), (or, tag)),
        #  ((free, tag), (or, tag), (don't, tag))
        #  ((or, tag), (don't, tag), (!, tag))]
        # In order to rebuild the string we need he middle words from each 3-gram as well as
        # the first word from the first 3-gram and the last word from the last 3-gram
        # Note: this is essentially replicating string.replace, but we want to ensure
        # replacement of the same occurance of the word as was chosen earlier.  
        words = [new_tokens[0][0]] + [token[1] for token in new_tokens] + [new_tokens[-1][2]]
        new_quote = " ".join([w[0] for w in words])
        new_quote = utils.cleanup_string(new_quote)

        quote_response = collections.namedtuple(
            "QuoteResponse", ["old_quote", "author", "new_quote"])
        randomized_quote = quote_response(
            old_quote=old_quote[0], author=author, new_quote=new_quote)

        return randomized_quote

    def switch_tokens(self, original_tokens, tokens_to_switch):
        """Given a tokenized quote and a list of tokens to switch, find a matching word for each
        switch token from the database and perform the switch. Returns a tokenized quote.
        Args:
            orignal_tokens (list): list of 3-grams of POS-tagged quote
            tokens_to_switch (list): list of tokens to replace, a subset of original tokens
        Return:
            A tokenized quote similar to orignal_tokens with tokens_to_switch replaced with
            new, POS-matching tokens. 
        """
        for switch_token in tokens_to_switch:
            old_word = switch_token[1][0]
            switch_tags = [token[1] for token in switch_token]

            # choose a new word with matching POS tags 
            replace_word_list = self.dbcontroller.get_matching_word_list(switch_tags)
            # Ensure we're not choosing the original word by removing from the response.
            # This will cause an IndexError if either the original word is not in the list
            # (pos_map is built from different data), or
            # it was only one item to choose from. In the latter case error is raised.
            try:
                replace_word_list.remove(old_word)
            except ValueError: 
                pass
            try:
                replace_word = random.choice(replace_word_list)
            except IndexError:
                raise IndexError("ERROR: couldn't find a replacing word")

            # find the index of the randomly selected switch token from the original tokenized quote
            idx = original_tokens.index(switch_token)  
            # switch_token is a tuple, convert to a mutable type since we want to modify the middle element
            switch_token = list(switch_token)
            switch_token[1] = (replace_word, "")  # new pos tag value is irrelevant
            original_tokens[idx] = switch_token

        return original_tokens

    def get_quote(self):
        return self.dbcontroller.get_quote()

    def get_fact(self):
        return self.dbcontroller.get_fact()

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
