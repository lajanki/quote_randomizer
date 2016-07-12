# quote_randomizer
Randomizes an actual quote by switching 1-3 words.

Random Quote Generator
A Python script that picks a random actual quote or a fact from a database, chooses 1-3 words and randomly
switches them to new ones. Uses a natural language toolkit module to tag
words into classes in order to choose a right type of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics line
by line, randomizes them and outputs the result.

Uses a database (quotes.db) to store and read quotes. The database consists
of 3 tables:
quotes: pairs of quotes and authors taken from real people, movies and
        games
lyrics: full lyrics to songs
dictionary: a table of words parsed from the other tables.


## Requirements

Python modules:
 * Natural Language Toolkit (nltk)
     http://www.nltk.org/index.html
 * sqlite3  (part of the standard library on newer Python versions)

Additionally the Tweeting feature requires:
 * Twython:
     https://twython.readthedocs.org/en/latest/

Keys:
 * You will need to register a Twitter app to get your own Twitter access tokens and developer keys, see https://dev.twitter.com/oauth/overview/application-owner-access-tokens Store these keys to the keys.json file.


## Usage

When run without any command line arguments the script generates a randomized quote to console window.
Command line arguments:

--rebuild-database [mode]
 *  Rebuilds the entire database by executing quotes.sql. Drops all previous data from quotes and lyrics but does not modify the dictionary. If no mode is set, the quotes and lyrics tables are parsed for new words to add to the dictionary. If mode is set to 'quick' the dictionary is not modified.
 *  If mode is set to 'quick', the dictionary is not modified.

--song
  * Randomizes the next song lyric from the database or nothing if the current song is finished. To advance to the next song generate at least one regular quote.

--tags
  * Shows info on all tags used to categorize words into classes.

--size
  * Shows the size of the databse.

--bot <mode>
  * If mode is set to 'quote', generates either a randomized quote or a fact and posts it to Twitter. If mode is 'song', processes the next song lyric from the current song and posts to Twitter.
  * Both modes require access tokens and API keys from Twitter.

--fact
  * Generate a randomized fact to print it on screen.


##### Maintenance commands
--init-song
  * Changes the status codes for the lyrics table back to initial values.

--set-song <name>
  * Sets the given song to be the next one read by the --song switch. See the 'search' column of the lyrics table for valid names.

--find-duplicates
  * Prints the first instance of quotes having a duplicate in the database.
  
--find-invalid
  * Finds database quotes which do not contain enough valid tags for switching.


## File structure

* quotes.py
  - The main script.
* dbaccess.py
  - an API to access the database.
* keys.json
  - An external file used to store Twitter access tokens and keys. Note that this file is just an empty shell to store your own keys. Only required for the tweeting component, ie. when running with '--bot quote' or '--bot song'.
* quotes.sql
  - A file used to create the database. Updating the database is done by manually updating this file and running the main script with the --rebuild-database switch.
* quotes.db
  - The databse containing three tables:
    1. quotes: a pair of (quote, author) records
    2. lyrics: a tuple of (title, search, verse, status) records, where
       * title, the title of the song
       * search, a search term given to the --set-song switch. Tells the main script to start this song the next time the --song switch is used. This is usually the same as title.
       * verse, a line or two of the actual lyrics. The purpose is to split the actual verses into small enough pieces to fit into a tweet.
       * status, whereas randomizing a quote is intended to happen by choosing a random quote from the database, song lyrics need to be processed in order. The satus code tells the script whether the last line of the song was encountered (satus code of 1). After the last line is processed the code changes to 2 telling the script to do nothing but wait for permission to move to the next song. Once at least one regular quote is generated the code changes to 3 and the next time the --song switch is used the script will start the next song.
    3. dictionary: a table of words parsed from the other two tables together with a tag identifying each word as a member of a specific word class. Using this tag a suitable word is chosen when randomizing quotes (ie. nouns get replaced by nouns, adjectives by adjectives etc.). The tag is determied by nltk.pos_tag() function.


#### Changelog
11.7.2016
* refactoring: moved general database query functions update_db(), parse_for_dictionary() and database_size() to their own module for easier access to other scripts utilizing the database.

24.2.2016
* removed the cumbersom START, END marking of quotes.sql. Instead all of quotes and lyrics are now parsed for the dictionary.
* cleaned up database creation down to a single function.
* added a dedicated function for parsing strings for valid words to add to the dictionary. Words with apostrophes and one letter words are not considered valid.
* changed find_invalid() function to reflect the above: it now also finds and deletes all one letter words and optionally deletes words with apostrophes.
* switch() now matches capitalization of the inserted word to the old word.

27.10.2015
* added ability to randomize facts

27.10.2015
* changed the argument parser class from optparse to argparse

31.8.2015
* initial relase

___
Written on Python 2.7.8

