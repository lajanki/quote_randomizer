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

    def __init__(self, path = "./"):
        """Define database connections and a base path for data files."""
        self.path = path
        self.con, self.cur = self.get_database_connection()

    def get_database_connection(self):
        """Try to create a connection to the database. Raises an error if it doesn't exist."""
        db_path = self.path + "quotes.db"

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
        """Given a list of tokenized words, choose words with matching pos tags from the database.
        Arg:
            tokens_to_change (list): a list of (idx, word, tag) tuples
        """
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
        Analyze the structure of the string and replace 1-3 words with ones fetched
        from database.
        Arg:
            string (string): the string to randomize
        Return:
            the new string
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
        s = " ".join(tokens)
        s = Randomizer.cleanup(s)

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


    @staticmethod
    def normalize_tokens(tokens):
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

    @staticmethod
    def cleanup(s):
        """Cleanup a string by removing extra whitespace around certain punctuation character.
        This whitespace is introduced when tokenizing a string.
        """
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
        for old, new in punctuation.iteritems():
            s = s.replace(old, new)

        return s


class QuoteRandomizer(Randomizer):
    """Randomizer for quotes and facts."""

    def __init__(self, path = "./"):
        Randomizer.__init__(self, path)

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
    Status of the current song (for a given SongRandomizer) is stored in a separate lyrics_status tables
    with the schema
        CREATE TABLE lyrics_status (name TEXT UNIQUE, current_song TEXT, current_row INTEGER);
    where name is a name given to the SongRandomizer and current_row is a row index to the lyrics table.
    """

    def __init__(self, name = "song_randomizer", path = "./"):
        """Init a randomizer together with a name to help determine the next line to processed
        from the database.
        """
        Randomizer.__init__(self, path)
        self.name = name

    def generate(self):
        """Fetch a lyric and randomize it."""
        lyric_record = self.get_next_lyric()
        title = lyric_record[0]
        lyric = lyric_record[1]

        randomized = self.randomize_string(lyric)
        return (title, randomized)

    def get_current_song_status(self):
        """Get current song status data from song_status table. Raises an Error if no song
        has been set (ie. previous song has been fully processed and waiting for call to start the next song).
        """
        with self.con:
            # Read current song status from lyrics_status table.
            self.cur.execute("SELECT current_song, current_row FROM lyrics_status WHERE name = ?", (self.name,))
            status = self.cur.fetchone()

        current_song = status[0]  # raises TypeError is self.name is not a valid database entry name
        current_row = status[1]

        if not current_song:
            raise SongError("No song set")

        return current_song, current_row

    def get_next_lyric(self):
        """Fetch the next lyric to be randomized. The next rowid to read is stored in the lyrics_status table.
        Raise an error is the next database row doesn't belong to the current song anymore.
        """
        current_song, current_row = self.get_current_song_status()
        with self.con:
            self.cur.execute("SELECT title, search, verse FROM lyrics WHERE rowid = ?", (current_row,))
            row_data = self.cur.fetchone()

            # check if we're out of the whole table (ie. finished the last song of the table)
            if not row_data:
                self.set_song_status("", -1) # next call to get_current_song_status will raise an error unless a valid song name is set
                raise SongError("Previous song finished")  # raise an error to stop execution

            # still within the current song
            elif not row_data[0] or row_data[0] == current_song:  # empty title denotes no song change
                # store the next row back to the database and change self.current_row
                self.set_song_status("", current_row + 1)
                return (row_data[0], row_data[2])  # return (title, lyric) -tuple

            # row belongs to the next song: store an empty value as current_song and raise an error to stop execution
            elif row_data[0] != current_song:
                self.set_song_status("", -1)
                raise SongError("Previous song finished")

    def set_song_status(self, song, rowid):
        """Update lyrics_status table with the provided song and rowid."""
        with self.con:
            self.cur.execute("UPDATE lyrics_status SET current_song = ?, current_row = ? WHERE name = ?", (song, rowid, self.name))

    def set_song(self, search_term):
        """Set the next song to be processed by get_next_lyric.
        Arg:
            search_term (string): determines the song to process next, one of the values in the search
            column of the lyrics table.
        """
        with self.con:
            self.cur.execute("SELECT rowid, title FROM lyrics WHERE search = ?", (search_term,))
            row = self.cur.fetchone()

            # Input didn't match to the table => print valid options on screen.
            if not row:
                raise SongError("No such song")

            # Update the status table
            else:
                self.set_song_status(row[1], row[0])
                print "Next song set to", search_term

    def get_songs(self):
        """Return a list of valid search terms to use with --set-song."""
        with self.con:
            self.cur.execute("SELECT search FROM lyrics")
            data = self.cur.fetchall()
            return [search[0] for search in data if search[0]] # drop empty strings

    def add_lyrics_status_entry(self):
        """Add an entry to the lyrics_status table for self.name."""
        with self.con:
            try: # name is UNIQUE
                self.cur.execute("INSERT INTO lyrics_status(name) VALUES (?)", (self.name,))
            except lite.IntegrityError as e:
                return


class SongError(Exception):
    """Custom error for song processing related edge cases."""
    pass
