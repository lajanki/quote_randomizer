#!/usr/bin/python
# -*- coding: utf-8 -*-

import quotes
import dbaccess
import nltk
import argparse

def main(args):
    """Process command line arguments."""

    # If no optional parameter was provided, also recreate the dictionary.
    if args.build_database:
        pass

    elif args.quote:
        randomize_quote()

    elif args.fact:
        randomize_fact()

    elif args.song:
        pass

    elif args.set_song:
        pass

    elif args.size:
        dbaccess.database_size()

    elif args.tags:
        nltk.help.upenn_tagset()


#============================================================================
# Define a function for each command line arg #
#==============================================
def build_quote_database():
    """Drop all existing data from quotes.db refill it by executing quotes.sql.
    TODO: switch for optional dictionary parsing?
    """
    dbaccess.create_quote_database()

def build_song_database():
    """Drop all existing data from songs.db refill it by executing songss.sql.
    TODO: switch for optional dictionary parsing?
    TODO: merge with above?
    """
    dbaccess.create_song_database()

def randomize_quote():
    """Create a new randomized quote or a fact."""
    randomizer = quotes.QuoteRandomizer()
    quote, author = randomizer.generate()
    print quote + "\n--" + author

def randomize_fact():
    """Create a new randomized fact."""
    randomizer = quotes.QuoteRandomizer()
    fact, _ = randomizer.get_fact()
    randomized = randomizer.randomize_string(fact)
    print fact


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A quote randomizer.")
    parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
    parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
    parser.add_argument("--song", help="Generate the next song lyric for the current song. Use --set-song to initialize a new song.", action="store_true")
    parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by --song. Use [list] to see valid choices.")
    parser.add_argument("--build-database", nargs="?", metavar="mode", const="full", help="""Fills the database by executing quotes.sql.
        If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary.
        If mode is set to 'quick' the dictionary is not modified.""")
    parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
    parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
    args = parser.parse_args()

    main(args)
