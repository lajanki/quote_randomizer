#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import random

from src import quotes
from src import utils


class RandomizeTestCase(unittest.TestCase):
    """Test cases for the base Randomizer class."""

    @classmethod
    def setUpClass(self):
        self.randomizer = quotes.Randomizer()

    def test_randomizer_changes_quotes(self):
        """Is randomized quote different from original?"""
        res = self.randomizer.generate()  # Note that this makes a real database access, does this matter?
        self.assertNotEqual(res.new_quote, res.old_quote)

    def test_randomized_quote_is_equal_word_length(self):
        """Is the string generated equal in word length to the original?"""
        res = self.randomizer.generate()
        new_quote_length = len(res.new_quote.split())
        old_quote_length = len(res.old_quote.split())

        self.assertEqual(new_quote_length, old_quote_length)

    def test_switch_tokens_replaces_words_with_matching_pos_tags(self):
        """Does switch_tokens replace selected tokens with words with the same POS tags as
        the original words?
        """
        quote = "The aim of education is the knowledge, not of facts, but of values."
        tokens = utils.tokenize_normalize_and_tag(quote)

        # ugh, copy-paste code from switch_tokens, maybe split into function?
        valid_tokens = [token for token in tokens if token[1][1] not in (".", "CUSTOM1")]
        change_degree = self.randomizer.get_change_degree(valid_tokens)
        tokens_to_switch = random.sample(valid_tokens, change_degree)

        modified_tokens = self.randomizer.switch_tokens(tokens, tokens_to_switch)
        original_tags = [token[1] for token in tokens]
        modified_tags = [token[1] for token in modified_tokens]

        self.assertEqual(original_tags, modified_tags)

    def test_change_degree_for_short_string(self):
        """The computed change degree for a short string should be 1"""
        tokens = "Short message".split()
        change_degree = self.randomizer.get_change_degree(tokens)
        self.assertEqual(change_degree, 1)

    def test_change_degree_in_range(self):
        """Is the change degree in [1,3]?"""
        tokens = "Oh, my this is a wonderful treat. I shall treasure this for at least a few seconds, possibly longer!".split()
        change_degree = self.randomizer.get_change_degree(tokens)
        self.assertGreaterEqual(change_degree, 1)
        self.assertLessEqual(change_degree, 3)

    @unittest.skip("Not implemented")
    def test_replace_keeps_capitalization(self):
        """Does switch_tokens keep capitalization?"""
        pass


if __name__ == "__main__":
    unittest.main()


