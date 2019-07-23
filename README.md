# quote_randomizer
Randomizes an actual quote by switching 1-3 words with ones of matching type.
> You must trust and believe in hardware or life becomes impossible.  
> --Anton Chekhov  
> original: You must trust and believe in people or life becomes impossible.



 This script uses the Natural Language Toolkit (nltk) module to split an orginal quote to part-of-speech tags (POS tags), such as nouns and verbs. Thus, randomization is done by replacing randomly chosen words with new words of same POS tags. New words are chosen from an internal nltk dataset. Quotes are picked from a local database collected from several sources, see below.

Since a word's POS tag is dependant on the context of the sentence around it, this script analyzes the quote in 3-grams, ie. replacing is done so that the new words orignally appeared in a context where the two adjacent words had the same POS tags as in the quote to randomize.  

Also includes a small Twython based Twitter bot for tweeting the results.

https://www.nltk.org/



## Usage
Install virtualenv and dependencies with
```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
To use the nltk module, some additional data is needed:
```
python -m nltk.downloader book
```
This includes a corpora and tokenizer, see https://www.nltk.org/data.html. Note: this will download some 400MB of data to `~/nltk_data`

To generate a randomized quote, run 
```
python main.py --quote
```

The full interface is as follows:
```
optional arguments:
  -h, --help            show this help message and exit
  --quote               Generate a randomized quote.
  --fact                Generate a randomized fact.
  --build-quote-database
                        Fills the database from quotes.txt.
  --size                Shows the size of the databse.
  --verbose             Print additional randomization information
  --tags                Shows info on all tags used to categorize words into
                        classes.
```

### Twitter bot
In order to use the Twitter bot, Twitter's API keys and access tokens are needed. Once (acquired)[https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html] they should be places in `keys.json`.

The bot can then be used with
```
python run_bot.py --tweet
```
This generates a randomized quote and tweets it.


### Unit tests
Unit tets can be run with
```
python -m unittest test/test_*.py
```


