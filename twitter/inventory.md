## Twitter scraping
For scraping twitter i use twint as there is no throttling or registration required. You can check the example script for the exact query i used: `scrape_twitter.sh` 

Also for preprocessing you can use the `preprocess_twitter.py` script based on pandas as an example, simply reads the hardcoded csv file and removes as much data as required to get only comic pages.

## Data files
- twk_comic_tweets.tsv data collected using twint, in tab separated format. 
- twk_comic_tweets.csv same as above but now true comma separated format
- twitter_only_comic.csv data collected and cleaning up.
