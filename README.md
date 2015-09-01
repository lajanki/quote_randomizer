# quote_randomizer
Randomizes an actual quote by switching 1-3 words.

Random Quote Generator                                         
A Python script that picks a random actual quote from a database, chooses 1-3 words and randomly
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


## Requires:

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

--rebuild-database
  * Rebuilds the entire database by executing quotes.sql. Drops previous data from quotes and lyrics and parses the sections marked by 'START' and 'END' for the dictionary (see quotes.sql). You need to manually edit this section to keep this script from dropping and re-inserting the same words to the dictionary everytime you use this switch ie. when adding new quotes to the database.

--rebuild-database quick
  * Rebuilds the database by executing quotes.sql. Does not modify the dictionary.

--song
  * Randomizes the next song lyric from the database or nothing if the current song is finished. To advance to the next song generate at least one regular quote.

--tags
  * Shows info on all tags used to categorize words into classes.

--size
  * Shows the size of the databse.

--bot quote
  * Generates a quote and posts it to Twitter. Requires access tokens and API keys from Twitter.

--bot song
  * Generates a song lyric and posts to Twitter. Requires access tokens and API keys from Twitter.

### Maintenance commands:
--init-song
  * Changes the status codes for the lyrics table back to initial values.

--set-song <name>
  * Sets the given song to be the next one read by the --song switch. See the 'search' column of the lyrics table for valid names.

--find-duplicates
  * Prints the first instance of quotes having a duplicate in the database.



## File structure

* quote.py
  - The main script.
* keys.json
  - An external file used to store Twitter access tokens and keys. Note that this file is just an empty shell to store your own keys. Only required for the tweeting component, ie. when running with '--bot quote' or '--bot song'.
* quote.sh
  - A Linux script to run quote.py. Automatically runs it again if the first try doesn't provide a valid quote.
* quotes.sql
  - A file used to create the database. Updating the database is done by manually updating this file and running the main script with the --rebuild-database switch.
* quotes.db
  - The databse containing three tables:
    - quotes: a pair of (quote, author) records
    - lyrics: a tuple of (title, search, verse, status) records, where
       * title, the title of the song
       * search, a search term given to the --set-song switch. Tells the main script to start this song the next time the --song switch is used. This is usually the same as title.
       * verse, a line or two of the actual lyrics. The purpose is to split the actual verses into small enough pieces to fit into a tweet.
       * status, whereas randomizing a quote is intended to happen by choosing a random quote from the database, song lyrics need to be processed in order. The satus code tells the script whether the last line of the song was encountered (satus code of 1). After the last line is processed the code changes to 2 telling the script to do nothing but wait for permission to move to the next song. Once at least one regular quote is generated the code changes to 3 and the next time the --song switch is used the script will start the next song.

___
* Tested on Python 2.7.8, the raw_input() call on line 501 will probably cause a syntax error on version 3. Otherwise should work on later versions as well.
* Lauri Ajanki 31.8.2015 
