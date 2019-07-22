#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Tweets quotes randomized by quotes.py.
https://twitter.com/quote_bot_6
"""


import json
import os
import argparse
import logging

import twython
from src import quotes
from src import utils


PATH_TO_LOG = os.path.join(utils.PATH_TO_SRC, "..", "bot_quotes.log")
PATH_TO_KEYS = os.path.join(utils.PATH_TO_SRC, "..", "keys.json")

logging.basicConfig(filename = PATH_TO_LOG, format="%(asctime)s %(message)s", level=logging.INFO)

with open(PATH_TO_KEYS) as f:
    data = json.load(f)
    API_KEY = data["API_KEY"]
    API_SECRET = data["API_SECRET"]
    OAUTH_TOKEN = data["OAUTH_TOKEN"]
    OAUTH_SECRET = data["OAUTH_SECRET"]

twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
randomizer = quotes.Randomizer()



def generate_tweet():
    """Generate a random quote using quotes module and format response as a tweet."""
    quote = randomizer.generate()

    if quote.author == "fact":
        msg = "Random non-fact:\n" + quote.new_quote
    else:
        msg = quote.new_quote + "\n" + "--" + quote.author

    return msg

def tweet(msg):
    """Tweets a message"""
    twitter.update_status(status = msg)
    logging.info(msg)






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Twitterbot for randomized quotes.")
    parser.add_argument("--tweet", action="store_true", help="Generate and tweet a randomized quote.")
    args = parser.parse_args()

    if args.tweet:
        msg = generate_tweet()
        tweet(msg)

