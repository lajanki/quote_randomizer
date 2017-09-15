#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
bot.py
Tweets quotes randomized by quotes.py.
Note: unlike main.py, this scripts provides little error checking. Database files are expected to exist
and generating lyrics will ungracefully exit if there is no next line to read.
"""

import twython
import json
import argparse
import logging

import quotes

logging.basicConfig(filename = "./quotes.log", format="%(asctime)s %(message)s", level=logging.INFO)
randomizer = quotes.QuoteRandomizer

def generate_randomized_message(mode):
    """Generate a radom quote or a song lyric using a corresponding Randomizer.
    Arg:
        mode (string): the type of message to generate, 'quote' for quote or a fact,
          or 'lyric' for a song lyric.
    Return
        the generated message
    """
    if mode == "quote":
        randomizer = quotes.QuoteRandomizer()
        quote, author = randomizer.generate()

        if author == "fact":
            msg = "Random non-fact:\n" + quote
        else:
            msg = quote + "\n" + "--" + author

    elif mode == "song":
        randomizer = quotes.SongRandomizer(name = "bot")
        # Randomze the next lyric. This raises (an uncaught!) SongError if the current song is fully processed
        # or no song has been set. In such case The song needs to be manually changed with the --set-song switch
        # before this does anything.
        song, lyric = randomizer.generate()

        # add the title to the first lyric
        if first_row:
            msg = song + "\n" + lyric
        else:
            msg = lyric

    else:
        raise ValueError("Invalid mode, recognized values are 'quote' and 'song'")

    return msg

def tweet(msg):
    """Tweets a message"""
    with open("./keys.json") as f:
        data = json.load(f)
        API_KEY = data["API_KEY"]
        API_SECRET = data["API_SECRET"]
        OAUTH_TOKEN = data["OAUTH_TOKEN"]
        OAUTH_SECRET = data["OAUTH_SECRET"]

    twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
    twitter.update_status(status = msg)
    logging.info(msg)

def set_song(song):
    """Set the next song to be processed by --song."""
    randomizer = quotes.SongRandomizer(name = "bot")

    # check input is a valid table in songs.db
    valid = randomizer.get_songs()
    if song == "list":
        for name in valid:
            print name

    elif song not in valid:
        print "ERROR: invalid entry, valid song names are:"
        for name in valid:
            print name

    else:
        randomizer.set_song_status(song)
        print "Current song set to {}. Use --tweet song to start tweeting".format(song)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Twitterbot for randomized quotes.")
    parser.add_argument("--tweet", metavar="mode", help="Generates and tweets a [quote] or a [song] lyric.", choices = ["quote", "song"])
    parser.add_argument("--set-song", metavar="song", help="""
        Sets the given song to be the next one read by --tweet song. Use 'list' to see valid choices.""")
    args = parser.parse_args()
    #print args

    if args.tweet:
        msg = generate_randomized_message(args.tweet)
        tweet(msg)

    elif args.set_song:
        set_song(args.set_song)
