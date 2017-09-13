#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
quote.py - A Random Quote Generator
Picks an actual quote or a fact from a database, chooses 1-3 words
and randomly switches them to new ones. Uses a natural language toolkit
module (nltk) to tag words into classes in order to choose a right type
of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics from another
database line by line, randomizes them and outputs the result.
"""


import nltk
import random
import os.path
import sqlite3 as lite

import dbaccess


class Randomizer:

    def __init__(self, path = "./"):
        """Define database connections and a base path for data files."""
        self.path = path
        # create connection to quotes.db, this is common to by both QuoteRandomizer and SongRandomizer
        self.con, self.cur = self.get_database_connection(path + "quotes.db")

    def get_database_connection(self, db_file):
        """Try to create a connection to a database. Raises an error if it doesn't exist."""

        # lite.connect will create an empty database if one doesn't exist, raise an error instead
        if not os.path.isfile(db_file):
            raise IOError("Error Database {} doesn't exist.".format(db_file))

        con = lite.connect(db_file)
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
        # create new connection to the song database, don't overwrite existing connector to quotes.db!
        self.song_con, self.song_cur = self.get_database_connection(path + "songs.db")
        # add an entry into the song_status table for self.name,
        # (ignored if one is already present)
        self.add_song_status_entry()

    def generate(self):
        """Fetch a lyric and randomize it."""
        song, lyric = self.get_next_lyric()

        randomized = self.randomize_string(lyric)
        return (song, randomized)

    def get_current_song_status(self):
        """Get current song status data (table name and row index) from song_status table. Raises an Error if no song
        has been set (ie. previous song has been fully processed and waiting for call to start the next song).
        """
        with self.song_con:
            # Read current song status from lyrics_status table.
            self.song_cur.execute("SELECT song, current_row FROM song_status WHERE name = ?", (self.name,))
            status = self.song_cur.fetchone()

        if not status:
            raise SongError("No song set")

        table = status[0]
        row = status[1]

        if not table:
            raise SongError("No song set")

        return table, row

    def get_next_lyric(self):
        """Fetch the next lyric to be randomized. The current song and the next rowid to read is read from the song_status table.
        Raise an error if the current song has been fully processed (or not set).
        """
        table, row = self.get_current_song_status() # get table name and row inedx of the table to read
        with self.song_con:
            sql = "SELECT verse FROM \"{}\" WHERE rowid = ?".format(table) # table names can't be targeted for a parameter replacements :(
            self.song_cur.execute(sql, (row,))
            row_data = self.song_cur.fetchone()

            # is the song already fully processed?
            if not row_data:
                self.set_song_status("", -1) # empty song_status data for clarity
                raise SongError("Previous song finished")  # raise an error to stop execution

            # still within the current song
            else:
                # update row index in song_status
                #self.set_song_status(row + 1)
                self.set_song_status(table, row + 1)
                return (table, row_data[0])  # return (title, lyric) -tuple

    def set_song_status(self, song, rowid = 1):
        """Update song_status table with the provided song and rowid.
        Note: caller should handle input validation.
        """
        with self.song_con:
            self.song_cur.execute("UPDATE song_status SET song = ?, current_row = ? WHERE name = ?", (song, rowid, self.name))

    def add_song_status_entry(self):
        """Add an entry to the lyrics_status table for self.name."""
        with self.song_con:
            try:
                # name is UNIQUE, song is NOT NULL, insert dummy data for song and current_row to denote invalid entry
                self.song_cur.execute("INSERT INTO song_status(name) VALUES (?)", (self.name,))
            except lite.IntegrityError as e:
                print "Using existing song_status entry for {}".format(self.name)

    def get_songs(self):
        """Return a list of valid song names to process, ie, the names of the tables in songs.db."""
        with self.song_con:
            self.song_cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            data = self.song_cur.fetchall()
            return [table_name[0] for table_name in data if table_name[0] != "song_status"] # drop song_status table




class SongError(Exception):
    """Custom error for song processing related edge cases."""
    pass
