# quote_randomizer
Randomizes an actual quote by switching 1-3 words with ones of matching type.
> You must trust and believe in hardware or life becomes impossible.  
> --Anton Chekhov  
>
> original: You must trust and believe in people or life becomes impossible.

This script uses the Natural Language Toolkit (nltk) module to split an orginal quote to part-of-speech tags (POS tags), such as nouns and verbs. Randomization is then done by replacing randomly chosen words with new words of same POS tags. New words are chosen from an internal `nltk` dataset. Quotes are chosen from a local `SQLite` database collected from several sources, see below.

Since a word's POS tag is dependant on the context of the sentence around it, this script analyzes the quote in 3-grams, ie. replacing is done so that the new words orignally appeared in a context where the two adjacent words had the same POS tags as in the quote to randomize.  

https://www.nltk.org/



## Usage
First, install dependencies in a virtualenv with
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To utilize the `nltk` module, some additional data is needed:
```bash
python -m nltk.downloader book
```
This includes a corpora and tokenizer, see https://www.nltk.org/data.html.

Then, build a database of quotes with
```bash
python main.py --build-database
```

Finally, generate a randomized quote with
```bash
python main.py --quote
```

## Unit tests
Unit tets can be run with
```bash
pytest
```

## Quote sources
The quote database is buit from the quotes in `data/quotes.txt`. This file contains a collection of quotes from people, books, movies, games
as well as facts, song lyrics, poem lines, proverbs and company slogans. These are collected from multiple online sources, including
* http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/
* http://www.cs.virginia.edu/~robins/quotes.html
* http://www.quotery.com/lists/top-500-greatest-quotes-of-all-time/
* http://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html
* http://www.notable-quotes.com/
* https://www.spec2000.net/06-basicphysics.htm
* http://www.quotegarden.com/
* http://www.adslogans.co.uk/site/pages/home/hall-of-fame.php
* http://www.hongkiat.com/blog/77-catchy-and-creative-slogans/
* http://www.goodreads.com/topic/show/1006385-1-000-random-facts
* https://www.reddit.com/r/quotes/
* https://en.wikipedia.org/wiki/AFIs_100_Years...100_Movie_Quotes
* http://www.thefactsite.com/2011/07/top-100-random-funny-facts.html
* http://www.cs.cmu.edu/~bingbin/
* https://www.reddit.com/r/funfacts/
