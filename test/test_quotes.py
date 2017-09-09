#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import nltk
import sys
import os
import sqlite3 as lite

sys.path.append("../")  # append the main script folder to sys.path to be able to import quotes from it
import quotes


class RandomizeTestCase(unittest.TestCase):
    """Test cases for the base Randomizer class."""

    @classmethod
    def setUpClass(self):
        """Create a randomizer."""
        self.randomizer = quotes.Randomizer("../")

    @classmethod
    def tearDownClass(self):
        del self.randomizer

    def testIOErrorOnInvalidPath(self):
        """Does trying to create a Generator object with non-existing path raise an error?"""
        path = "noSuchPath"
        self.assertRaises(IOError, quotes.Randomizer, path)

    def testChangeDegreeForShortString(self):
        """The computed change degree for a short string should be 1"""
        tokens = "Short message".split()
        change_degree = self.randomizer.get_change_degree(tokens)
        self.assertEqual(change_degree, 1)

    def testChangeDegreeInRange(self):
        """Is the change degree in [1,3]?"""
        tokens = "Oh, my this is a wonderful treat. I shall treasure this for at least a few seconds, possibly longer!".split()
        change_degree = self.randomizer.get_change_degree(tokens)
        self.assertGreaterEqual(change_degree, 1)
        self.assertLessEqual(change_degree, 3)

    def testChooseReplacingWordsKeepsNumberOfWordsIntact(self):
        """Does choose_replacing_words generate equal number of replacing words as was passed in?"""
        tokens =  [(0, "carbon", "NN"), (1, "feeling", "NN")]
        replacing_words = self.randomizer.choose_replacing_words(tokens)
        self.assertEqual(len(replacing_words), 2)

    def testChooseReplacingWordsKeepsCapitalizationAndIndicesIntact(self):
        """Does choose_replacing_words keep capitalization and word indices intact?"""
        tokens =  [(0, "Carbon", "NN"), (1, "FEELING", "NN")]
        replacing_words = self.randomizer.choose_replacing_words(tokens)

        # first word
        self.assertEqual(replacing_words[0][0], 0)
        word = replacing_words[0][1]
        self.assertEqual(word, word.capitalize())

        # second word
        self.assertEqual(replacing_words[1][0], 1)
        word = replacing_words[1][1]
        self.assertEqual(word, word.upper())

    def testChooseReplacingWordsKeepsPOSTagsIntact(self):
        """Does choose_replacing_words replace with the same POS tag?"""
        tokens =  [(0, "green", "JJ"), (1, "carbon", "NN")]
        replacing_words = self.randomizer.choose_replacing_words(tokens)

        # use nltk to find out the new words' tags
        new_words = [token[1] for token in replacing_words]
        tagged = nltk.pos_tag(new_words)

        tag1 = tagged[0][1]
        self.assertEqual(tag1, "JJ")
        tag2 = tagged[1][1]
        self.assertEqual(tag2, "NN")

    def testWordSwitching(self):
        """Do the correct words get switched in switch_word_tokens?"""
        original = "Big Bertha on the long and winding street".split()
        new_tokens = [(0, "Small"), (2, "against"), (6, "relaxing"), (7, "pavement")]
        expected = "Small Bertha against the long and relaxing pavement".split()

        switched = self.randomizer.switch_word_tokens(original, new_tokens)
        self.assertEqual(switched, expected)

    def testRandomizedStringIsEqualLength(self):
        """Is the string generated equal in length to the original?"""
        s = "Sometimes winter never comes, other times James's birthday is in July, but never after the fifth."
        new = self.randomizer.randomize_string(s)
        self.assertEqual(len(s.split()), len(new.split()))

    def testRandomizingRaisesErrorOnInvalidInput(self):
        """Does randomize_string raise ValueError if there are no valid words in the input?"""
        s = ", !!! :) http"
        self.assertRaises(ValueError, self.randomizer.randomize_string, s)

    def testNormalization(self):
        """Does token normalization remove extra whitespace around a single quote?"""
        tokens = "Bender 's game".split()
        s = " ".join(quotes.Randomizer.normalize_tokens(tokens))

        self.assertEqual(s, "Bender's game")

    def testStringCleanup(self):
        """Does cleanup remove whitespace around punctuation?"""
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

        self.assertEqual(quotes.Randomizer.cleanup(s1), s1_expected)
        self.assertEqual(quotes.Randomizer.cleanup(s2), s2_expected)
        self.assertEqual(quotes.Randomizer.cleanup(s3), s3_expected)
        self.assertEqual(quotes.Randomizer.cleanup(s4), s4_expected)
        self.assertEqual(quotes.Randomizer.cleanup(s5), s5_expected)


class QuoteRandomizerTestCase(unittest.TestCase):
    """QuoteRandomizer test cases."""

    @classmethod
    def setUpClass(self):
        """Create a randomizer."""
        self.randomizer = quotes.QuoteRandomizer("../")

    @classmethod
    def tearDownClass(self):
        del self.randomizer

    def testRandomizedQuoteNotTheSame(self):
        """Is the generated quote different from the original quote?"""
        quote, author = self.randomizer.get_quote()
        randomized = self.randomizer.randomize_string(quote)

        self.assertNotEqual(quote, randomized)


@unittest.skip("Old behaviour")
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
