#!/bin/bash

# Forum
python3 analyze_interactions.py forum/forumQuery-2021-04-18_13\:40\:26.csv --category replies --sigma 2 --out graphs/forum_replies.png > descriptors/forum_replies.txt
python3 analyze_interactions.py forum/forumQuery-2021-04-18_13\:40\:26.csv --category views --sigma 2 --out graphs/forum_views.png > descriptors/forum_views.txt
