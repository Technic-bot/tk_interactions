import pandas as pd 

df_twk = pd.read_csv('twitter/twk_comic_tweets.tsv',delimiter='\t')
df_twk.drop_duplicates('id',inplace=True)
df_twk['tweet'] = df_twk['tweet'].str.strip()
q = df_twk['tweet'].str.contains('http',case=False)
q2 = df_twk['tweet'].str.contains('comic',case=False)
q_no_at = df_twk['tweet'].str.contains('@')
q_no_gift = df_twk['tweet'].str.contains('giftart',case=False)
q_no_sketch = df_twk['tweet'].str.contains('sketch',case=False)

real_comic = df_twk[q & q2 & ~q_no_at & ~q_no_gift & ~q_no_sketch]

real_comic.to_csv('twitter/twitter_only_comic.csv')

