#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
A library module for creating and adding new items to the base databases for the randomizers.
"""

import os
import sys
import nltk
import sqlite3 as lite

import quotes

CLASSES = quotes.Randomizer.CLASSES

def create_quote_database():
    """Drop all current data from quotes.db and refill it from quotes.sql"""
    try:  # the file may not exist
        os.remove("quotes.db")
    except OSError as e:
        pass

    con, cur = get_connection("quotes.db")
    with con:
        cur.execute("CREATE TABLE quotes (quote TEXT UNIQUE NOT NULL, author TEXT NOT NULL, frequency INTEGER DEFAULT 0)")
        cur.execute("CREATE TABLE dictionary (word TEXT, class TEXT, UNIQUE(word, class))")

    execute_sql("quotes.sql")
    build_dictionary()

def create_song_database():
    """Drop all current data from songs.db and refill it from songs.sql."""
    try:  # the file may not exist
        os.remove("songs.db")
    except OSError as e:
        pass

    execute_sql("songs.sql")  # contains CREATE TABLE statements

def execute_sql(sql_file):
    """Execute the contents of quotes.sql or songs.sql to update the corresponding database.
    Arg:
        sql_file (string): the file to execute, the correct database is determined from the filename.
    """
    db_file = os.path.splitext(sql_file)[0] + ".db"
    con, cur = get_connection(db_file)

    with con:
        print "Executing {}, please wait...".format(sql_file)
        with open(sql_file) as f:
            lines = [line.rstrip("\n;").lstrip("\t") for line in f]
            for sql in lines:
                # quotes column in quotes.db is UNIQUE, skip duplicate lines. This also skips
                # existing lines when adding new quotes to the database via quotes.sql.
                # songs.db may contain duplicated lyrics
                try:
                    cur.execute(sql)
                except (lite.Warning, lite.IntegrityError) as e:
                    pass
                except Exception as e:
                    print e
                    print "Something went wrong, try rebuilding the database"
                    sys.exit() # stop execution as soon as an unknown error occurs

def build_dictionary():
    """Builds the dictionary table by reading the tagged data from Brown corpus from the nltk module
    and inserts that data to the database. This corpus has a total of ~ 1.1 million (word, tag) pairs
    with ~ 42 000 valid pairs to enter in the database.
    """
    con, cur = get_connection("quotes.db")

    print "Building a dictionary from an internal dataset. This may take a while..."
    tagged = nltk.corpus.brown.tagged_words()
    # Strip multiples and words with invalid tags and characters.
    # It's sligthly faster to first remove multiples and then remove invalid.
    tagged = set(tagged)
    tagged = [token for token in tagged if ( token[1] in CLASSES and token[0].replace("-", "").isalnum() and len(token[0]) > 3 )]

    print "Inserting " + str(len(tagged)) + " items to the database."
    with con:
        for word, tag in tagged:
            if tag in CLASSES:
                try:
                    cur.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))
                except lite.IntegrityError as e:
                    pass

def parse_table_for_dictionary():
    """Parse the quotes table for words to add to the dictionary table."""
    con, cur = get_connection("quotes.db")

    new_tokens = []
    with con:
        cur.execute("SELECT quote FROM quotes")
        quotes = cur.fetchall()

        for quote in quotes:
            tagged = pos_tag_string(quote[0])
            for item in tagged:
                new_tokens.append(item)

        # strip multiples
        new_tokens = list(set(new_tokens))

        # add to the dictionary
        try:
            cur.executemany("INSERT INTO dictionary(word, class) VALUES(?, ?)", new_tokens)
        except lite.IntegrityError as e:
            pass

def parse_string_for_dictionary(s):
    """Parse given string for database dictionary. Exclude words already in the dictionary.
    Args:
        s (string): the string to parse
    """
    con, cur = get_connection("quotes.db")

    tagged = pos_tag_string(s)
    if not tagged:
        print "No valid tags in:"
        print s

    # Store in database.
    with con:
        for word, tag in tagged:
            if tag in CLASSES:
                try:  # the (word, tag) needs to be unique
                    cur.execute("INSERT INTO dictionary(word, class) VALUES(?, ?)", (word, tag))
                except lite.IntegrityError as e:
                    pass

#==================================================================
# Helper functions #
#==================#

def get_connection(db_file):
    """Helper function: create a connection to a database."""
    con = lite.connect(db_file)
    cur = con.cursor()

    return con, cur

def pos_tag_string(s):
    """Use nltk to pos-tag a string. Strips invalid and short words.
    Valid tokens to insert to the database:
        1) may contain "-", otherwise alphanumeric
        2) len > 3
    """
    tokens = nltk.word_tokenize(s)
    tokens = quotes.Randomizer.normalize_tokens(tokens) # stich apostrophes back: let's -> [let, 's].
    tagged = nltk.pos_tag([word.lower() for word in tokens])
    tagged = [token for token in tagged if (token[0].replace("-", "").isalnum() and len(token[0]) > 3) ]

    return tagged

def database_size():
    """Print information on the size of the database.
    Used with --size switch.
    """
    con = lite.connect("quotes.db")
    cur = con.cursor()

    with con:
        cur.execute("SELECT COUNT(quote) FROM quotes")
        size = cur.fetchone()
        print size[0], "quotes"

        cur.execute("SELECT COUNT(*) FROM dictionary")
        size = cur.fetchone()
        print size[0], "words"

        for item in CLASSES:
            cur.execute("SELECT COUNT(word) FROM dictionary WHERE class = ?", (item,))
            size = cur.fetchone()
            print item, size[0]

def find_invalid():
    """Find various erroneous entries from of quotes.sql (not the database!):
      1 long (quote, author)-pairs
      2 duplicates
      3 uses of "'" as a quote character, (should only be used as an apostrophe)
    Note: finding long quotes is not entirely reliable as the randomized quote may still be too long to tweet.
    Return:
        a dict of lists for each type of invalid entries.
    """
    long_ = []
    apostrophes = []
    dupes = []
    seen = []
    with open("quotes.sql") as f:
        for line in f:
            if line == "\n" or line.startswith("--"):  # skip empty lines and comments
                continue

            # Strip the sql from the beginning and the end.
            line = line.lstrip("INSERT INTO quotes(quote, author) VALUES") # Note that this still leaves a "'" (but not a space or "(" !) to the beginning...
            line = line.lstrip("'")  # remove the single quote separately, this way no actual quote characters are removed
            line = line.rstrip("');\n" )  # remove sql characters and any whitespace from the end
            # Split by "'," combination to get the individual items from the (quote, author)-pair
            quote, author = line.split("',")

            if quote in seen:
                dupes.append(quote)
            seen.append(quote)

            # Is it too long?
            if len(quote + author) > 135:
                long_.append(quote)

            # Look for quotes containing double apostrophes not followed by any of the valid suffixes
            suffix = ("s", "t", "m", "d", "ll", "re", "ve")
            #suffix = ["''" + s for s in suffix]
            if "''" in quote and not any(["''"+s in quote for s in suffix]):
                apostrophes.append(quote)

    return {"dupes": dupes, "long": long_, "apostrophes": apostrophes}
