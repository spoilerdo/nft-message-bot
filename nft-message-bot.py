import tweepy
import json
from time import sleep
from credentials import *
from config import MAX_RESULT, QUERY, MESSAGE, SLEEP_TIME

client = tweepy.Client(bearer_token, consumer_key,
                       consumer_secret, access_token, access_token_secret)

print('retrieving recent tweets...')

tweets = client.search_recent_tweets(
    QUERY, max_results=MAX_RESULT).data  # type: ignore
# json.dumps(tweets, indent=2)

print(f'retrieved {tweets.count}')

for tweet in tweets:
    try:
        print('tweeting!')

        client.create_tweet(text=MESSAGE, in_reply_to_tweet_id=tweet.id)
        sleep(SLEEP_TIME)
    except StopIteration:
        break
