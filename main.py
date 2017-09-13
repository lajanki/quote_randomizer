#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A runnable interface to quotes.py. Prints generated quotes/songs on screen."""

import quotes
import dbaccess
import nltk
import argparse
import sys

def main(args):
    """Process command line arguments."""
    if args.build_quote_database:
        build_quote_database()

    elif args.build_song_database:
        build_song_database()

    elif args.quote:
        randomize_quote()

    elif args.fact:
        randomize_fact()

    elif args.song:
        randomize_lyric()

    elif args.set_song:
        set_song(args.set_song)

    elif args.size:
        print "quotes.db contains:"
        dbaccess.database_size()

    elif args.tags:
        nltk.help.upenn_tagset()


#============================================================================
# Define a function for each command line arg #
#==============================================
def build_quote_database(mode):
    """Drop all existing data from quotes.db refill it by executing quotes.sql."""
    # check for invalid entries in quotes.sql before creating the database
    invalid = dbaccess.find_invalid()
    critical = invalid["dupes"] + invalid["dupes"]
    if critical:
        print """ERROR: found the following invalid entries in quotes.sql.
        Check for extra whitespace and duplicates and try again."""
        for item in critical:
            print item
        sys.exit()

    print "Creating quotes.db"
    dbaccess.create_quote_database()

    if mode == "full":
        print "Parsing quotes for the dictionary, this may take a while..."
        # TODO: parsing
        # 1 get quotes from db
        # 2 pos-tag separately
        # 3 group tagged words to a dict
        # 4 insert the lists to the dictionary

def build_song_database():
    """Drop all existing data from songs.db and refill it by executing songs.sql.
    TODO: switch for optional dictionary parsing?
    """
    print "Creating songs.db"
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

def randomize_lyric():
    """Randomize the next lyric for the default song randomizer (ie. name == song_randomizer)"""
    randomizer = quotes.SongRandomizer()
    try:
        title, lyric = randomizer.generate()
        print lyric
    except quotes.SongError as err:
        print "Previous song finished. User --set-song to initialize the next song and try again."
        raise

def set_song(song):
    """Set the next song to be processed by --song."""
    randomizer = quotes.SongRandomizer()

    # check input is a valid table in songs.db
    valid = randomizer.get_songs()
    if song == "list":
        for name in valid:
            print name

    elif song not in valid:
        """Invalid entry, valid song names are:"""
        for name in valid:
            print name

    else:
        randomizer.set_song_status(song)
        print "Current song set to {}. Use --song to start processing it.".format(song)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A quote randomizer.")
    parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
    parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
    parser.add_argument("--song", help="Generate the next song lyric for the current song. Use --set-song to initialize a new song.", action="store_true")
    parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by --song. Use 'list' to see valid choices.")
    parser.add_argument("--build-quote-database", nargs="?", metavar="mode", const="quick", help="""Fills the database by executing quotes.sql.
        If mode is set to 'full', the quotes table are parsed for new words to add to the dictionary.
        By default, the dictionary is not modified.""")
    parser.add_argument("--build-song-database", action="store_true")
    parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
    parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
    args = parser.parse_args()

    main(args)
