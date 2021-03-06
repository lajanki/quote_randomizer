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

    elif args.tags:
        show_universal_tagset()



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

def show_universal_tagset():
    print("Universal tagset, https://www.nltk.org/book/ch05.html")
    print("""
        Tag	Meaning             English Examples
        ADJ	adjective	    new, good, high, special, big, local
        ADP	adposition	    on, of, at, with, by, into, under
        ADV	adverb	            really, already, still, early, now
        CONJ    conjunction	    and, or, but, if, while, although
        DET	determiner, article the, a, some, most, every, no, which
        NOUN	noun	            year, home, costs, time, Africa
        NUM	numeral	            twenty-four, fourth, 1991, 14:24
        PRT	particle	    at, on, out, over per, that, up, with
        PRON	pronoun	            he, their, her, its, my, I, us
        VERB	verb	            is, say, told, given, playing, would
        .	punctuation         . , ; !
        X	other	            ersatz, esprit, dunno, gr8, univeristy
    """)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A quote randomizer.")
    parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
    parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
    parser.add_argument("--build-quote-database", action="store_true", help="Fills the database from quotes.txt.")
    parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
    parser.add_argument("--verbose", help="Print additional randomization information", action="store_true")
    parser.add_argument(
        "--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
    args = parser.parse_args()

    db = dbcontroller.Controller()
    main(args)
