#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
bot.py
Tweets quotes randomized by quotes.py


Change log:
21.3.2017
 *  Small changes to how song lyrics are processed to reflect the changes in quotes.py.
17.3.2017
 *  Initial version.
"""



import sys
import twython
import json
import argparse
import logging

import quotes



if __name__ == "__main__":
	logging.basicConfig(filename = quotes.path + "quotes.log", format="%(asctime)s %(message)s", level=logging.INFO)


	parser = argparse.ArgumentParser(description="A quote randomizer.")
	parser.add_argument("--tweet", metavar="mode", help="Generates a [quote] or a [song] lyric and posts it to Twitter. Requires access tokens and API keys from Twitter.")
	parser.add_argument("--set-song", metavar="song", default="list", help="Sets the given song to be the next one read by --tweet song. Use [list] to see valid choices.")

	args = parser.parse_args()
	#print args


	#=========#
	# --tweet #
	#=========#
	if args.tweet:
		msg = ""
		mode = args.tweet
		if mode not in ["quote", "song"]:
			print "Error: invalid mode, please use either 'quote' or 'song'."
			sys.exit()

		# Format the message of the tweet based on whether the database item was a quote or a fact.
		if mode == "quote":
			quote = quotes.get_quote()
			randomized_quote = quotes.randomize(quote)

			if randomized_quote[1] == "fact":
				msg = "Random non-fact:\n" + randomized_quote[0]
			else:
				msg = randomized_quote[0] + "\n" + "--" + randomized_quote[1]

		else: 	# mode == "song"
			title, lyric = randomize_lyric()

			if title:
				msg = title + "\n" + lyric
			else:
				msg = lyric


		with open(quotes.path+"keys.json") as f:
			data = json.load(f)
			API_KEY = data["API_KEY"]
			API_SECRET = data["API_SECRET"]
			OAUTH_TOKEN = data["OAUTH_TOKEN"]
			OAUTH_SECRET = data["OAUTH_SECRET"]

		twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
		twitter.update_status(status = msg)
		logging.info(msg)

	#============#
	# --set song #
	#============#
	elif args.set_song:
		if args.set_song == "list":
			for name in quotes.get_songs():
				print name

		else:
			quotes.set_song(args.set_song)









