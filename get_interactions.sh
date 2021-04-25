# Forum
python3 analyze_interactions.py forum/forumQuery-2021-04-18_13\:40\:26.csv --category replies --sigma 2 --out graphs/forum_replies.png > descriptors/forum_replies.txt
python3 analyze_interactions.py forum/forumQuery-2021-04-18_13\:40\:26.csv --category views --sigma 2 --out graphs/forum_views.png > descriptors/forum_views.txt

# Twitter
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category retweets_count --sigma 2  --title tweet --out graphs/twitter_only_retweets.png > descriptors/twitter_only_retweets.txt
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category likes_count --sigma 2  --title tweet --out graphs/twitter_only_likes.png > descriptors/twitter_only_likes.txt
python3 analyze_interactions.py twitter/twitter_only_comic.csv --category replies_count --sigma 2  --title tweet --out graphs/twitter_only_replies.png > descriptors/twitter_only_replies.txt

# Reddit
python3 analyze_interactions.py reddit/comic-pruned-2021-04-22.csv --category score --sigma 2 --out graphs/reddit_score.png > descriptors/reddit_score.txt
python3 analyze_interactions.py reddit/comic-pruned-2021-04-22.csv --category comments --sigma 2 --out graphs/reddit_comments.png > descriptors/reddit_comments.txt
python3 analyze_interactions.py reddit/combined.csv --category score --sigma 2 --out graphs/reddit_score_combined.png >descriptors/reddit_score_combined.txt
python3 analyze_interactions.py reddit/combined.csv --category comments --sigma 2 --out graphs/reddit_comments_combined.png >descriptors/reddit_comments_combined.txt

