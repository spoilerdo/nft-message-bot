import tweepy
import json
from time import sleep
from credentials import *
from config import MAX_RESULT, QUERY, MESSAGE, SLEEP_TIME

client = tweepy.Client(bearer_token, consumer_key,
                       consumer_secret, access_token, access_token_secret)

tweets = client.search_recent_tweets(QUERY, max_results=MAX_RESULT).data
json.dumps(tweets, indent=2)

for tweet in tweets:
    try:
        client.create_tweet(text=MESSAGE, in_reply_to_tweet_id=tweet.id)
    except StopIteration:
        break
