#!/bin/bash

python3 analyze_interactions.py reddit/comic-pruned-2021-04-22.csv --category score --sigma 2 --out graphs/reddit_score.png > descriptors/reddit_score.txt
python3 analyze_interactions.py reddit/comic-pruned-2021-04-22.csv --category comments --sigma 2 --out graphs/reddit_comments.png > descriptors/reddit_comments.txt
python3 analyze_interactions.py reddit/combined.csv --category score --sigma 2 --out graphs/reddit_score_combined.png >descriptors/reddit_score_combined.txt
