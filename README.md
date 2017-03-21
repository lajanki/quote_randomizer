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
 * Twython:
     https://twython.readthedocs.org/en/latest/

Keys:
 * Using the bot feature requires Twitter access tokens and developer keys, see https://dev.twitter.com/oauth/overview/application-owner-access-tokens. These keys should be stored in keys.json file.


## Usage

The main module ```quotes.py``` can be run directly for example usage:
```
  --quote               Generate a randomized quote.
  --fact                Generate a randomized fact.
  --update-database [mode]
                        Fills the database by executing quotes.sql. If no mode
                        is set, the quotes and lyrics tables are parsed for
                        new words to add to the dictionary. If mode is set to
                        'quick' the dictionary is not modified.
  --size                Shows the size of the databse.
  --tags                Shows info on all tags used to categorize words into
                        classes.
```
The Twitterbot in ```bot.py``` generates and tweets randomized quotes and song lyrics. Using it requires valid Twitter access tokens and keys stored in ```keys.json```. 
```
  --tweet mode     Generates a [quote] or a [song] lyric and posts it to
                   Twitter. Requires access tokens and API keys from Twitter.
  --set-song song  Sets the given song to be the next one read by --tweet
                   song. Use [list] to see valid choices.
```


## File structure

* quotes.py
  - The main script.
* bot.py
  - Twitterbot
* dbaccess.py
  - an API to access the database.
* keys.json
  - An external file used to store Twitter access tokens and keys. The provided file is just an empty shell to store your own keys. Only required when running bot.py.
* quotes.sql
  - SQL statements to create the database. Updating the database is done by manually updating this file and running the main script with the ```--rebuild-database``` switch.
* quotes.db
  - The databse containing three tables:
    1. quotes: with columns (quote, author) of actual quotes read from various internet sources, see quotes.sql.
    2. lyrics: with columns (title, search, verse, status), where
       * title, the title of a song
       * search, a shorter version of title used to tell --set-song which song should be processed next
       * verse, a line or two of the actual lyrics. The purpose is to split the actual verses into small enough pieces to fit into a tweet.
       * status, a leftover from previous version. Will probably be removed later...
    3. dictionary: with columns (word, class) of pos-tagged words used to identify valid words for the randomizer to use. Most of the contents are pulled from the nltk library.



___
Written on Python 2.7.8

