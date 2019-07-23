#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Project entrypoint. Prints generated quotes/songs on screen.
"""

import argparse
import sys

import nltk
from src import quotes
from src import dbcontroller


def main(args):
    """Process command line arguments."""
    if args.build_quote_database:
        build_quote_database()

    elif args.quote:
        randomize_quote()

    elif args.fact:
        randomize_fact()

    elif args.size:
        print("quotes.db contains:")
        db.get_size()

    #TODO: display correct tagset
    elif args.tags:
        nltk.help.upenn_tagset()


# ============================================================================
# Define a function for each command line arg #
# ==============================================
def build_quote_database():
    """Drop all existing data from quotes.db refill it from quotes.txt."""
    # First, check quotes.txt integrity, raises ValueError if not valid
    db.validate_quotes()

    print("Creating quotes.db")
    db.create_quote_database()

    print("Adding quotes to the dictionary, this may take a while...")
    db.insert_quotes()
    db.insert_pos_map()

def randomize_quote():
    """Create a new randomized quote or a fact."""
    try:
        randomizer = quotes.Randomizer()
        res = randomizer.generate()
        quote = res.new_quote
        author = res.author

        print(quote + "\n--" + author)
        if args.verbose:
            print("original:", res.old_quote)

    except IOError as err:
        print("ERROR: database doesn't exist, create it with --build-quote-database")

def randomize_fact():
    """Create a new randomized fact."""
    try:
        randomizer = quotes.Randomizer()
        res = randomizer.generate("fact")
        fact = res.new_quote

        print(fact)
        if args.verbose:
            print("original:", res.old_quote)

    except IOError as err:
        print("ERROR: database doesn't exist, create it with --build-quote-database")





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A quote randomizer.")
    parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
    parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
    parser.add_argument("--build-quote-database", action="store_true", help="""Fills the database from quotes.txt.""")
    parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
    parser.add_argument("--verbose", help="Print additional randomization information", action="store_true")
    parser.add_argument(
        "--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
    args = parser.parse_args()

    db = dbcontroller.Controller()
    main(args)
