import os.path

import collections
import nltk
from nltk.corpus import brown


PATH_TO_SRC = os.path.abspath(os.path.dirname(__file__))
PATH_TO_DB = os.path.join(PATH_TO_SRC, "..", "quotes.db")
PATH_TO_QUOTES_TXT = os.path.join(PATH_TO_SRC, "..", "data", "quotes.txt")

# determine the tagset to use for determining POS tags,
# see https://github.com/slavpetrov/universal-pos-tags
NLTK_TAGSET = "universal"


def tokenize_normalize_and_tag(quote):
    """Tokenize and POS-tag a quote to a a list of 3-grams.
    Args:
        quote (string) the quote to POS-tag
    Return:
        list of POS-tagged 3-grams    
    """
    tokens = nltk.word_tokenize(quote)
    normalized_tokens = normalize_tokens(tokens)
    normalized_tags = pos_tag_and_normalize(normalized_tokens)

    ngrams = nltk.ngrams(normalized_tags, 3)
    # ngrams is a generator, return a list (quotes are short anyway)
    return list(ngrams)

def normalize_tokens(tokens):
    """nltk.word_tokenize() will tokenize words with ' as an apostrophe into
    two tokens: eg. "can't" -> ["can", "'t"]. This causes problems when choosing words to replace.
    This function normalizes tokens by reattaching the parts back together.
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

def pos_tag_and_normalize(normalized_tokens):
    """POS tag normalized tokens. After the apostrophe has been stiched back together, nltk.pos_tag
    will likely generate unreliable tags for such words. This function manually sets POS tags to a specific value
    for all tokens containning a ' character.
    """
    tags = nltk.pos_tag(normalized_tokens, tagset=NLTK_TAGSET)
    for idx, token in enumerate(tags):
        if "'" in token[0]:
            # tokens are tuples, create a new token with custom POS tag and replace the old one
            new_token = (token[0], "CUSTOM1")
            tags[idx] = new_token

    return tags

def create_pos_map():
    """Create a defaultdict of 3 consecutive POS tags and matching middle words from an nltk
    internal dataset. The key is a ;-delimited string of the POS tags.
    Eg. finds all verbs with NUM, VERB, PRON sequence in the dataset.
    """
    index = collections.defaultdict(set)
    brown_tagged_sents = brown.tagged_sents(categories="news", tagset=NLTK_TAGSET)

    # create 3-grams from each sentence
    for sent in brown_tagged_sents:

        # set POS tag for words with apostrophes to CUSTOM1
        for idx, token in enumerate(sent):
            if "'" in token[0]:
                # tokens are tuples, create a new token with custom POS tag and replace the old one
                new_token = (token[0], "CUSTOM1")
                sent[idx] = new_token

        ngrams = nltk.ngrams(sent, 3)
        for ngram in ngrams:
            # join the 3 POS tags from each ngram as key to the index
            key = ";".join([token[1] for token in ngram])
            word = ngram[1][0]  # middle word as the value

            index[key].add(word)

    return index

def cleanup_string(s):
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
