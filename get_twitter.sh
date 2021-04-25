#!/bin/bash
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category retweets_count --sigma 2  --title tweet --out graphs/twitter_only_retweets.png > descriptors/twitter_only_retweets.txt
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category likes_count --sigma 2  --title tweet --out graphs/twitter_only_likes.png > descriptors/twitter_only_likes.txt
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category replies_count --sigma 2  --title tweet --out graphs/twitter_only_replies.png > descriptors/twitter_only_replies.txt

