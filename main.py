#!/usr/bin/python
# -*- coding: utf-8 -*-

	def main(self, args):
		"""Process command line arguments."""

		# If no optional parameter was provided, also recreate the dictionary.
		if args.update_database:
			quick = False
			mode = args.update_database # check for optional parameter, if none default to 'full'

			if mode not in ["full", "quick"]:
				print "Error: invalid mode, please use either 'full' (default) or 'quick'."
				sys.exit()

			if mode == "quick":
				quick = True
			if mode == "full":
				ans = raw_input("The database will be parsed for new words in the dictionary.\
				This may take some time, continue? (y/N)\n")
				if ans != "y":
					print "Exiting."
					sys.exit()

			dbaccess.update_db(quick)

		elif args.quote:
			quote = self.get_quote()
			rand = self.randomize(quote)
			print rand[0] + "\n--" + rand[1]

		elif args.fact:
			fact = self.get_fact()
			rand = self.randomize(fact)
			print rand[0] + "\n--" + rand[1]

		elif args.song:
			lyric = self.randomize_lyric()
			if lyric[0]:
				print lyric[0] + "\n" + lyric[1]
			else:
				print lyric[1]

		elif args.set_song:
			if args.set_song == "list":
				for name in self.get_songs():
					print name

			else:
				self.set_song(args.set_song)

		elif args.size:
			dbaccess.database_size()

		elif args.tags:
			nltk.help.upenn_tagset()




if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A quote randomizer.")
	parser.add_argument("--quote", help="Generate a randomized quote.", action="store_true")
	parser.add_argument("--fact", help="Generate a randomized fact.", action="store_true")
	parser.add_argument("--song", help="Generate the next song lyric for the current song. Use --set-song to initialize a new song.", action="store_true")
	parser.add_argument("--set-song", metavar="song", help="Sets the given song to be the next one read by --song. Use [list] to see valid choices.")
	parser.add_argument("--update-database", nargs="?", metavar="mode", const="full", help="""Fills the database by executing quotes.sql.
		If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary.
		If mode is set to 'quick' the dictionary is not modified.""")
	parser.add_argument("--size", help="Shows the size of the databse.", action="store_true")
	parser.add_argument("--tags", help="Shows info on all tags used to categorize words into classes.", action="store_true")
	args = parser.parse_args()

	app = Randomizer()
	try:
		app.main(args)
	# switch() had nothing to switch (no valid tags)
	except ValueError as e:
		print e
