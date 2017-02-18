#This programs is for retrieving tweets from a particular hashtag

import json
import TwitterLogin
import os
import codecs

twitter_api = TwitterLogin.login_twitter1()
iterator = twitter_api.statuses.sample()
iterator1 = twitter_api.statuses.filter(track="Travel", result_type='recent', language="en")
# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 5
tweet_count1 = 5
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print("First Loop   ",json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break

for tweet in iterator1:
    tweet_count1 -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print("Second Loop  ", json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count1 <= 0:
        break