#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
quote.py - A Random Quote Generator
Picks a random actual quote or a fact from a database, chooses 1-3 words
and randomly switches them to new ones. Uses a natural language toolkit
module (nltk) to tag words into classes in order to choose a right type
of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics line
by line, randomizes them and outputs the result.

Uses a database (quotes.db) to store and read quotes. The database consists
of 3 tables:
  * quotes: pairs of quotes and authors taken from real people, movies and
    games
  * lyrics: full lyrics to songs
  * dictionary: a table of words parsed from the other tables.
"""



import sys
import argparse
import nltk
import random
import os.path
import sqlite3 as lite

import dbaccess


class Randomizer:

    def __init__(self):
        """Define database connections.
        Arg:
            name (string): instance name, separates normal usage of database resources from
                how the bot uses them. (Mainly keeps the bot's lyrics table status
                separate from the data when running this script on it's own)
        """
        self.con, self.cur = self.get_database_connection()

    def get_database_connection(self):
        """Try to create a connection to the database. Raises an error if it doesn't exist."""
        db_path = "quotes.db"

        # lite.connect will create an empty database if one doesn't exist, raise an error instead
        if not os.path.isfile(db_path):
            raise IOError("Error Database quotes.db doesn't exist. Use --init to create it.")

        con = lite.connect(db_path)
        cur = con.cursor()

        return con, cur

    def get_change_degree(self, tokens):
        """Given a tokenized string, determine the number of words to change."""
        if len(tokens) < 4:
            return 1 # for short strings only change 1 word

        rand = random.random()
        if rand <= 0.65:
            change_degree = 1
        elif rand <= 0.93:
            change_degree = 2
        else:
            change_degree = 3
        return change_degree

    def choose_replacing_words(self, tokens_to_change):
        """Given a list of tokenized words, choose words with matching pos tags from the database."""
        new_words = []
        with self.con:
            for token in tokens_to_change:
                self.cur.execute("SELECT word  FROM dictionary WHERE class = ? AND word != ? ORDER BY RANDOM()", (token[2], token[1]))
                db_word = self.cur.fetchone()[0]

                # capitalize the word if necessary:
                if token[1] == token[1].upper():  # the whole word should be capitalized
                    db_word = db_word.upper()

                elif token[1] == token[1].capitalize(): # only the first letter is capitalized
                    db_word = db_word.capitalize()

                new_word_token = (token[0], db_word)  # (idx, word) -tuple
                new_words.append(new_word_token)

        return new_words

    def switch_word_tokens(self, tokenized_string, new_tokens):
        """Given tokenized string and a lists of word tokens, replace words whose index
        match those in the latter list.
        """
        for token in new_tokens:
            idx = token[0]
            tokenized_string[idx] = token[1]

        return tokenized_string

    def randomize_string(self, string):
        """Perform the actual randomizing of the given string.
        Analyze the structure of the string, replace 1-3 words with ones fetched
        from database.
        Arg:
            string (string): the string to randomize
        Return:
            a dict of the randomized string, words replaced and words inserted
        """
        # tokenize, reattach apostrophes and pos tag tokens
        tokens = Randomizer.normalize_tokens(nltk.word_tokenize(string))
        tagged = nltk.pos_tag(tokens)

        invalid_tokens = [
            "'",
            "http",
            "@",
            "//",
            "#",
            "%"
        ]

        # format a list of (idx, word, tag) tuples of valid tokens in tagged
        valid = [ (idx, item[0], item[1]) for idx, item in enumerate(tagged)
            if not any(token in item[0] for token in invalid_tokens) and item[1] in dbaccess.CLASSES ]

        if not valid:
            raise ValueError("Error: no valid words to change.\n" + string)

        # determine the words to change, fetch matching words from the database and make the switch
        change_degree = self.get_change_degree(valid)
        words_to_change = random.sample(valid, change_degree) # list of (idx, word, tag) tuples of words from the original string
        replacing_words = self.choose_replacing_words(words_to_change) # list of (idx, word) tuples of new words
        tokens = self.switch_word_tokens(tokens, replacing_words)

        # join the tokens back together and trim extra whitespace around punctuation
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
        s = " ".join(tokens)
        for old, new in punctuation.iteritems():
            s = s.replace(old, new)

        return s

    def create_database(self):
        """Create the database tables and use dbaccess module to fill it."""
        with self.con:
            cur.execute("CREATE TABLE quotes (quote TEXT UNIQUE NOT NULL, author TEXT NOT NULL, frequency INTEGER DEFAULT 0)")
            cur.execute("CREATE TABLE dictionary (word TEXT, class TEXT, UNIQUE(word, class))")
            cur.execute("CREATE TABLE lyrics (title TEXT, search TEXT UNIQUE, verse TEXT)")
            cur.execute("CREATE TABLE lyrics_status (name TEXT UNIQUE, current_song TEXT, current_row INTEGER)")

        dbaccess.update_db()
        dbaccess.build_dictionary()
        parser.print_help()

    def generate(self):
        """Create a randomized string from a database entry. This method should be implemented in a subclass."""
        pass


    @classmethod
    def normalize_tokens(self, tokens):
        """nltk.word_tokenize() will tokenize words using ' as an apostrophe into
        two tokens: eg. "can't" -> ["can", "'t"].
        This function normalizes tokens by reattaching the parts back together. This will prevent
        switch() from choosing the prefixes to be switched (words with apostrophes would be rejected anyway).
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
                print e

        normalized = [token for token in tokens if token != "DEL"]
        return normalized


class QuoteRandomizer(Randomizer):
    """Randomizer for quotes and facts."""

    def __init__(self):
        Randomizer.__init__(self)

    def generate(self):
        """Choose a random quote or fact from the database and randomized it."""
        quote, author = self.get_quote()
        randomized = self.randomize_string(quote)

        return (randomized, author)

    def get_quote(self):
        """Fetch a random quote or a fact from the database.
        Return:
            (quote, author) tuple
        """
        with self.con:
            self.cur.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
            row = self.cur.fetchone()

            # update the frequency column
            frequency = row[2] + 1
            quote = row[0]
            self.cur.execute("UPDATE quotes SET frequency=? WHERE quote=?", (frequency, quote))

        return (row[0], row[1])

    def get_fact(self):
        """Fetch a random fact from the database.
        Return:
            (fact, "fact") tuple
        """
        with self.con:
            self.cur.execute("SELECT * FROM quotes WHERE author=? ORDER BY RANDOM() LIMIT 1", ("fact",))
            fact = self.cur.fetchone()[0]

            return (fact, "fact")


class SongRandomizer(Randomizer):
    """Randomizer for song lyrics. Keeps track of which lyrics was previously fetched from the database
    so whole songs are processed in order.
    """

    def __init__(self, name):
        """Init a randomizer together with a name to help determine the next line to processed
        from the database.
        """
        Randomizer.__init__(self)
        self.name = name

    def generate(self):
        """Fetch a lyric and randomize it."""
        lyric_record = self.get_next_lyric()
        if lyric_record:
            title = lyric_record[0]
            lyric = lyric_record[1]

            randomized = self.switch(lyric)["randomized"]
            return (title, randomized)

    def get_next_lyric(self):
        """Each song in the lyrics table is meant to be processed line-by-line. This functions returns the
        next line of lyrics to be processed by switch().
        The rowid of the database row to read is stored in the status (ie. first) line of the lyrics table.
        Calls sys.exit() if the next line of lyrics is from another song.
        Return:
            A tuple of (title, lyric) the lyric read from the database or None if the previous song has
            been fully processed. The tile of a song is != None only for the first lyric of each song
                denoting a change in song.
        """
        with self.con:
            # Read current song status from lyrics_status table.
            self.cur.execute("SELECT * FROM lyrics_status WHERE name = ?", (self.name,))
            status = self.cur.fetchone()
            current_title = status[1]
            current_row = status[2]

            if not current_title:
                print "No song set, initialize new song with python bot.py --set-song and try again."  # only bot.py has the proper switch
                return  # returns None. This is followed by sys.exit() in randmize_lyric()

            # Fetch the row to process.
            self.cur.execute("SELECT * FROM lyrics WHERE rowid = ?", (current_row,))
            data = self.cur.fetchone()

            # Was there a row to fetch?
            if not data:
                self.cur.execute("UPDATE lyrics_status SET current_song = ? WHERE name = ?", (None, self.name)) # empty current_song
                print "Current song finished, initialize a new song with python bot.py --set-song and try again."
                return

            # Row belongs to current song => return (title, lyric)-pair and increment row index in the status row.
            elif not data[0] or data[0] == current_title:
                self.cur.execute("UPDATE lyrics_status SET current_row = ? WHERE name = ?", (current_row + 1, self.name))
                return (data[0], data[2])  # title (ie. data[0]) is !None only for the first line of each song

            # Row starts a new song => clear title from the status row and prompt for a song change.
            elif data[0] != current_title:
                self.cur.execute("UPDATE lyrics_status SET current_song = ? WHERE name = ?", (None, self.name))
                print "Current song finished, initialize a new song with --set-song and try again."
                return

    def set_song(self, search_term):
        """Set the next song to be processed by get_next_lyric().
        Arg:
            search_term (string): the song to process next, one of the values in the search
            column of the lyrics table.
        """
        with self.con:
            self.cur.execute("SELECT rowid, title FROM lyrics WHERE search = ?", (search_term,))
            row = self.cur.fetchone()

            # Input didn't match to the table => print valid options on screen.
            if not row:
                print "Invalid option."
                valid = self.get_songs()  # opens another database connection! (is this bad?)
                print "Valid options (case sensitive):"
                for name in valid:
                    print name

            # Update the status row with the title and start row index of the selected song.
            else:
                self.cur.execute("UPDATE lyrics_status SET current_song=?, current_row=? WHERE name=?", (row[1], row[0], self.name))
                print "Next song set to", search_term

    def get_songs(self):
        """Return a list of valid search terms to use with --set-song."""
        with self.con:
            self.cur.execute("SELECT search FROM lyrics")
            data = self.cur.fetchall()
            return [search[0] for search in data if search[0]] # drop empty strings

    def add_lyrics_status_entry(self):
        """Add a new entry to the lyrics_status table for self.name if
        not already present.
        """
        with self.con:
            try: # name is UNIQUE, return if self.name is already present
                cur.execute("INSERT INTO lyrics_status(name) VALUES (?)", (self.name,))
            except lite.IntegrityError as e:
                return
