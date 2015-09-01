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

---------
Requires:
---------
Python modules:
 * Natural Language Toolkit (nltk)
     http://www.nltk.org/index.html
 * sqlite3  (should come with a newer version of python)
Additionally the Tweeting feature requires:
 * Twython:
     https://twython.readthedocs.org/en/latest/
 Keys:
 * You will need to register a Twitter app to get your own Twitter access tokens and developer keys, see
     https://dev.twitter.com/oauth/overview/application-owner-access-tokens      

-----
Usage
-----
When run without any command line arguments the script generates a randomized quote to console window.
command line arguments:
--rebuild-database
    Rebuilds the entire database by executing quotes.sql. Drops previous data from quotes and lyrics and parses the sections marked by 'START' and 'END' for the dictionary (see quotes.sql). You need to manually edit this section to keep this script from dropping and re-inserting the same words to the dictionary everytime you use this switch ie. when adding new quotes to the database.
--rebuild-database quick
    Rebuilds the database by executing quotes.sql. Does not modify the dictionary.
--song
    Randomizes the next song lyric from the database or nothing if the current song is finished. To advance to the next song generate at least one regular quote.
--tags
    Shows info on all tags used to categorize words into classes.
--size
    Shows the size of the databse.
--bot quote
    Generates a quote and posts it to Twitter. Requires access tokens and API keys from Twitter.
--bot song
    Generates a song lyric and posts to Twitter. Requires access tokens and API keys from Twitter.

Maintenance commands:
--init-song
    Changes the status codes for the lyrics table back to initial values.
--set-song <name>
Sets the given song to be the next one read by the --song -switch. See the 'search' column of the lyrics table for valid names.
  --find-duplicates
Prints the first instance of quotes having a duplicate in the database.


--------------
File structure
--------------
* quote.py
   -The main script.
* keys.json
   -An external file used to store Twitter access tokens and keys. Note that this file is just a shell to store your own keys. Only required for the tweeting component, ie. when running with '--bot quote' or '--bot song'.
* quote.sh
   -A Linux script to run quote.py. Automatically runs it again if the first try doesn't provide a valid quote.
* quotes.sql
   -A file used to create the database. Updating the database is done by manually updating this file and running the main script with the --rebuild-database switch.
* quotes.db
   -The databse. Contains three tables: quotes, lyrics and dictionary with creation schemas of
quotes: a pair of (quote, author) records
   lyrics: a tuple of (title, search, verse, status) records, where
     -title is the title of the song
     -search is the <name> in --set-song <name> switch and used to tell the main script to use this song as the one to process next. This is usually the same as title.
     -verse is a a part of the lyric. The actual verses of the song are split into small enough parts to fit into a tweet.
     -status, an integer telling the main script that this is the last line of the current song. The intended usage of the --song switch is to process the song in order until it's finished, (as opposed to the behavior with quotes where a random quote is chosen). The status codes tell the main script whether its processing the last line and whether it's OK to move to the next. Once a song is finished, you need to generate at least one regular quote to allow the --song switch to move on to the next song.

Tested on Python 2.7.8
Lauri Ajanki 31.8.2015 
