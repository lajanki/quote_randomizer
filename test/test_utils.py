from unittest.mock import Mock

import nltk
from src import utils



def test_normalize_tokens_joins_apostrophes():
    """Does normalize_tokens join tokens split by an apostrophe?"""
    quote = "Somehow this can't be incorrect. We shan't believe it!"
    tokens = nltk.word_tokenize(quote) 
    normalized_tokens = utils.normalize_tokens(tokens)

    expected = ["Somehow", "this", "can't", "be", "incorrect", ".", "We", "shan't", "believe", "it", "!"]
    assert normalized_tokens == expected

def test_pos_tag_and_normalize_sets_custom_tag_to_apostrophed_words():
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

    assert res == expected

def test_cleanup_string_removes_whitespace_before_punctuation():
    """Does cleanup_string remove punctuation before ceratin punctuation characters
    caused by tokenization?
    """
    s1 = "Win , for me !"
    assert utils.cleanup_string(s1) == "Win, for me!"

    s2 = "some guy @ babylon # sweet"
    assert utils.cleanup_string(s2) == "some guy @babylon #sweet"

    s3 = "http: //www.somesite.com"
    assert utils.cleanup_string(s3) == "http://www.somesite.com"

    s4 = "this be a `` quote''"
    assert utils.cleanup_string(s4) == "this be a \"quote\""

    s5 = "The Vindicators : Tomorrow's game"
    assert utils.cleanup_string(s5) == "The Vindicators: Tomorrow's game"

