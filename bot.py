#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
bot.py
Tweets quotes randomized by quotes.py


Change log:
17.3.2017
 *  initial version
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
	parser.add_argument("--init-song", help="Changes the status codes for the lyrics table back to initial values.", action="store_true")
	parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by the '--song' switch. See the search column of the lyrics table for valid names.")
	parser.add_argument("--tweet", metavar="mode", help="Generates a quote or a song lyric and posts it to Twitter. Requires access tokens and API keys from Twitter.")

	args = parser.parse_args()
	#print args


	###############
	# --init-song #
	###############
	# Change the status codes of the lyrics table back to initial values.
	if args.init_song:
		con = quotes.con
		cur = quotes.cur

		with con:
			# set all end-of-song codes back to 1
			cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
			# set the row index back to the first row of the first song
			cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (2, 1))
		print "Done"


	##############
	# --set-song #
	##############
	# Attempt to set the song provided as a command line argument to be the next one read from the database.
	elif args.set_song:
		con = quotes.con
		cur = quotes.cur

		with con:
			cur.execute("SELECT rowid FROM lyrics WHERE search = ?", (args.set_song,))
			row = cur.fetchone()

			if row == None:
				print "Invalid song"
				sys.exit(1)
			else:
				cur.execute("UPDATE lyrics SET status=? WHERE status=? OR status=?", (1,2,3))
				cur.execute("UPDATE lyrics SET status=? WHERE rowid=?", (row[0], 1))

	###########
	# --tweet #
	###########
	elif args.tweet:
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
			randomized_lyric = quotes.randomize_lyric()
			title = randomized_lyric[0]
			lyric = randomized_lyric[1]
			if title != None:
				msg = randomized_lyric[0]+"\n"+randomized_lyric[1]
			else:
				msg = randomized_lyric[1]


		with open(quotes.path+"keys.json") as f:
			data = json.load(f)
			API_KEY = data["API_KEY"]
			API_SECRET = data["API_SECRET"]
			OAUTH_TOKEN = data["OAUTH_TOKEN"]
			OAUTH_SECRET = data["OAUTH_SECRET"]

		twitter = twython.Twython(API_KEY, API_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
		twitter.update_status(status = msg)
		logging.info(msg)








