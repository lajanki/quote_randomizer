# A library module for interacting with the quote database.

import collections
import logging
import random
import sqlite3 as lite

from src import utils


class Controller:

    def __init__(self):
        self.con = lite.connect(utils.PATH_TO_DB)
        self.cur = self.con.cursor()

    def create_quote_database(self):
        """Creates the two tables _quotes_ and _pos_map_ for quotes and a mapping of POS
        classes and words. Drops all previous data!
        """
        with self.con:
            try:
                self.cur.execute("DROP TABLE quotes")
                self.cur.execute("DROP TABLE pos_map")
            except lite.OperationalError: # raised if tables don't exist
                pass

            self.cur.execute("CREATE TABLE quotes (quote TEXT UNIQUE, author TEXT)")
            self.cur.execute("CREATE TABLE pos_map (pos_id TEXT PRIMARY KEY, match_word TEXT)")

    def insert_quotes(self):
        """INSERT quotes from quotes.txt to the database. Skips existing quotes."""
        quote_tokens = self.parse_quotes()
        with self.con:
            # quote column is UNIQUE, skip duplicate lines.
            try:
                self.cur.executemany("INSERT INTO quotes VALUES (? ,?)", quote_tokens)
            except (lite.Warning, lite.IntegrityError):
                pass

    def insert_pos_map(self):
        """Fill pos_map table by creating the mapping and INSERTing in to the database."""
        pos_map = utils.create_pos_map()
        with self.con:
            for key in pos_map:
                match_words = ";".join(pos_map[key])

                self.cur.execute("INSERT INTO pos_map VALUES (?, ?)", (key, match_words))

    def get_quote(self):
        """SELECT and return a random (quote, author) tuple from the database."""
        try:
            with self.con:
                self.cur.execute("SELECT * FROM quotes ORDER BY RANDOM()")
                row = self.cur.fetchone()
        except lite.OperationalError as e:
            raise RuntimeError("database doesn't exist, create it with --build-database") from e

        return row

    def get_fact(self):
        """SELECT and return a random fact from the database."""
        try:
            with self.con:
                self.cur.execute("SELECT * FROM quotes WHERE author='fact' ORDER BY RANDOM()")
                row = self.cur.fetchone()
        except lite.OperationalError as e:
            raise RuntimeError("database doesn't exist, create it with --build-database") from e

        return row

    def get_matching_word_list(self, key):
        """Given a ;-delimited POS tag key, return all matching words from the pos_map
        table as a list. 
        """
        # if key is a list, convert to ;-delimited string
        if isinstance(key, list):
            key = ";".join(key)

        with self.con:
            self.cur.execute(
                "SELECT match_word FROM pos_map WHERE pos_id = ?", (key,))
            row = self.cur.fetchone()

        if not row:
            raise KeyError("Invalid key: {}".format(key))

        return row[0].split(";")

    def get_matching_word(self, key):
        """Given a ;-delimited POS tag key, return a random matching word from the pos_map
        table as a list. 
        """
        # if key is a list, convert to ;-delimited string
        if isinstance(key, list):
            key = ";".join(key)

        with self.con:
            self.cur.execute(
                "SELECT match_word FROM pos_map WHERE pos_id = ?", (key,))
            row = self.cur.fetchone()

        if not row:
            raise KeyError("Invalid key: {}".format(key))

        # row is a singleton tuple of ;-delimited string of all words matching the key, select one randomly
        rand_word = random.choice(row[0].split(";"))
        return rand_word

    def parse_quotes(self):
        """Fetch list of(quote, author) tuples from quotes.txt to be inserted into the database."""
        with open(utils.PATH_TO_QUOTES_TXT) as f:
            lines = f.readlines()

        # strip comments and empty lines
        lines = [line.rstrip("\n").split(";")
                 for line in lines if line != "\n" and not line.startswith("--")]

        return lines

    def validate_source_data(self):
        """Check quotes.txt for duplicates or otherwise malformed data."""
        invalid = self._find_invalid()
        total = invalid.duplicates + invalid.invalid
        if total:
            logging.warning("""Found the following invalid entries in quotes.txt.
            Check for extra whitespace and duplicates and try again.""")
            for item in total:
                print(item)

            raise ValueError("Invalid data in quotes.txt")

    def _find_invalid(self):
        """Find various types of invalid entries in quotes.txt (not from the database!).
        Each quote should:
          1 be short enough to fit in a tweet
          2 be ;-seprated as quote;author
          3 be unique
        Note: finding long quotes is not entirely reliable as the randomized quote may still be too long to tweet.
        Return:
            a dict of lists for each type of invalid entries.
        """
        long_ = []
        invalid = []
        dupes = []
        seen = []

        lines = self.parse_quotes()
        for line in lines:
            # too long?
            if len(" ".join(line)) > 135:
                long_.append(line)

            # ;-separated into two?
            if len(line) != 2:
                invalid.append(line)

            # duplicates?
            quote = line[0]
            if quote in seen:
                dupes.append(quote)
            seen.append(quote)

        InvalidQuoteContainer = collections.namedtuple(
            "InvalidQuoteContainer", ["duplicates", "long", "invalid"])
        return InvalidQuoteContainer(duplicates=dupes, long=long_, invalid=invalid)

    def get_size(self):
        """Print information on the size of the database.
        Used with --size switch.
        """
        with self.con:
            self.cur.execute("SELECT COUNT(quote) FROM quotes")
            size = self.cur.fetchone()

            return size[0]
