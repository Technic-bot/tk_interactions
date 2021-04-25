#!/bin/bash
# Example usage to scrape twitter api using twint
twint -u twokinds -o twk_tweets.json --json 
twint -u twokinds -o twk_comic_tweets.json --json --search comic
twint -u twokinds -o twk_comic_tweets.csv --csv --search comic

