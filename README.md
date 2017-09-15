# quote_randomizer
Randomizes an actual quote by switching 1-3 words to ones with matching type. The script chooses 1-3 words, selects replacing words from a database and stiches the quote back together. Uses a natural language toolkit module to tag words into classes in order to choose a right type of words to be replaced.

Can also be used to work with song lyrics: the script reads lyrics from a song database line
by line, randomizes them and outputs the result. 


## Requirements

Python modules:
 * Natural Language Toolkit (nltk)
     http://www.nltk.org/index.html
 * Twython:
     https://twython.readthedocs.org/en/latest/

Keys:
 * Using the bot feature requires Twitter access tokens and developer keys, see https://dev.twitter.com/oauth/overview/application-owner-access-tokens. These keys should be stored in keys.json file.


## Usage

The main module ```main.py``` supports the following switches:
```
  --quote               Generate a randomized quote.
  --fact                Generate a randomized fact.
  --song                Generate the next song lyric for the current song. Use
                        --set-song to initialize a new song.
  --set-song song       Sets the given song to be the next one read by --song.
                        Use 'list' to see valid choices.
  --build-quote-database [mode]
                        Fills the database by executing quotes.sql. If mode is
                        set to 'full', the quotes table are parsed for new
                        words to add to the dictionary. By default, the
                        dictionary is not modified.
  --build-song-database
  --size                Shows the size of the databse.
  --tags                Shows info on all tags used to categorize words into
                        classes.
```

```bot.py``` is a Twitterbot for tweeting the generated quotes. Using it requires valid Twitter access tokens and keys stored in ```keys.json```. 
```
  --tweet mode     Generates a [quote] or a [song] lyric and posts it to
                   Twitter. Requires access tokens and API keys from Twitter.
  --set-song song  Sets the given song to be the next one read by --tweet
                   song. Use [list] to see valid choices.
```
The ```--set-song``` switches are separate for both modules. In order to process a song the script needs to read it from the database line by line on each subsequent use of either ```quotes.py --song``` or ```bot.py --tweet song```. The status data is stored separately and using the main module will not affect which line the bot reads next.

## File structure
* main.py
  - The main script
* quotes.py
  - library module for creating quotes and song lyrics
* bot.py
  - Twitterbot
* dbcontroller.py
  - module for database creation related functions
* keys.json
  - A keyfile for Twitter access tokens. Store your own keys here. Only required when running bot.py
* quotes.sql
  - SQL statements for the quotes database. Updating the database is done by manually updating this file and running the main script with the ```--build-quote-database``` switch
* songs.sql
  - SQL statements for the song database, similar to above
* quotes.db
  - the quote database. Contains tables for actual quotes as well a dictionary table where replacing words are chosen
* songs.db
  - song database



___
Written on Python 2.7.8

