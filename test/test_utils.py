#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import nltk
from src import utils


class UtilsTestCase(unittest.TestCase):
    """Test cases for utils module."""

    def test_normalize_tokens_joins_apostrophes(self):
        """Does normalize_tokens join the 2 tokens split by apostrophe?"""
        quote = "Somehow this can't be incorrect. We shan't believe it!"
        tokens = nltk.word_tokenize(quote) 
        normalized_tokens = utils.normalize_tokens(tokens)

        expected = ["Somehow", "this", "can't", "be", "incorrect", ".", "We", "shan't", "believe", "it", "!"]
        self.assertEqual(normalized_tokens, expected)

    def test_pos_tag_and_normalize_sets_custom_tag_to_apostrophed_words(self):
        """Does pos_tag_and_normalize set POS tag to CUSTOM1 for words with apostrophes?"""
        quote = "Somehow this can't be incorrect. We shan't believe it!"
        tokens = nltk.word_tokenize(quote) 
        normalized_tokens = utils.normalize_tokens(tokens)
        res = utils.pos_tag_and_normalize(normalized_tokens)

        expected = [
            ('Somehow', 'ADV'),
            ('this', 'DET'),
            ("can't", 'CUSTOM1'),
            ('be', 'VERB'),
            ('incorrect', 'ADJ'),
            ('.', '.'),
            ('We', 'PRON'),
            ("shan't", 'CUSTOM1'),
            ('believe', 'VERB'),
            ('it', 'PRON'),
            ('!', '.')
        ]

        self.assertEqual(res, expected)



    def test_cleanup_string_removes_whitespace_before_punctuation(self):
        """Does cleanup_string remove punctuation before ceratin punctuation characters
        caused by tokenization?
        """
        s1 = "Win , for me !"
        s1_expected = "Win, for me!"

        s2 = "some guy @ babylon # sweet"
        s2_expected = "some guy @babylon #sweet"

        s3 = "http: //www.somesite.com"
        s3_expected = "http://www.somesite.com"

        s4 = "this be a `` quote''"
        s4_expected = "this be a \"quote\""

        s5 = "The Vindicators : Tomorrow's game"
        s5_expected = "The Vindicators: Tomorrow's game"

        self.assertEqual(utils.cleanup_string(s1), s1_expected)
        self.assertEqual(utils.cleanup_string(s2), s2_expected)
        self.assertEqual(utils.cleanup_string(s3), s3_expected)
        self.assertEqual(utils.cleanup_string(s4), s4_expected)
        self.assertEqual(utils.cleanup_string(s5), s5_expected)


if __name__ == "__main__":
    unittest.main()


