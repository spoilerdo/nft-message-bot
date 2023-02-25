import os
import tweepy
from time import sleep
from credentials import *
from config import *


def getenv(key):
    secret = os.environ.get(key)
    if (secret):
        return secret
    else:
        print(f'environment variable with key: {key} does not exist')
        return ''


print('initializing system...')

bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

if os.getenv('CI'):
    print('running in pipeline environment')

    bearer_token = getenv('BEARER_TOKEN')
    consumer_key = getenv('CONSUMER_KEY')
    consumer_secret = getenv('CONSUMER_SECRET')
    access_token = getenv('ACCESS_TOKEN')
    access_token_secret = getenv('ACCESS_TOKEN_SECRET')
else:
    print('running in local environment')

    bearer_token = BEARER_TOKEN
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET

client = tweepy.Client(bearer_token, consumer_key,
                       consumer_secret, access_token, access_token_secret)

print('retrieving recent tweets...')

tweets = client.search_recent_tweets(
    QUERY, max_results=MAX_RESULT, sort_order='relevancy').data  # type: ignore

print(f'retrieved {tweets.count}')

if DAYS >= MAX_DAYS
    INDEX += 1

DAYS += 1

for tweet in tweets:
    try:
        for nft in NFTS:
            print(f'tweeting for: {nft.name} NFT!')
            try:
                message = MESSAGES[INDEX].replace('${{SHORT_LINK}}', nft.short_url)
                client.create_tweet(
                    text=message, in_reply_to_tweet_id=tweet.id)
            except StopIteration:
                break
    except StopIteration:
        break
