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
 * Natural Language Toolkit
     http://www.nltk.org/index.html
Additionally the Tweeting feature requires:
 * Twython:
     https://twython.readthedocs.org/en/latest/
 Keys:
 * You will need to register a Twitter app to get your own Twitter access tokens and developer keys, see
     https://dev.twitter.com/oauth/overview/application-owner-access-tokens      

-----
Usage
-----
When run without any command line arguments the script generates a randomized quote to console window

Lauri Ajanki 31.8.2015 
