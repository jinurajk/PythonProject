import json
import TwitterLogin
from collections import Counter

#This method is used for Twitter login, defined in TwitterPgm3.py
twitter_api = TwitterLogin.login_twitter()

# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.
q = '#lufthansa'
count = 1000
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets
search_results = twitter_api.search.tweets(q=q, count=count)
#print("This is search_results", search_results)
statuses = search_results['statuses']
#print("This is statusues",statuses)
# Iterate through 5 more batches of results by following the cursor
for _ in range(5):
    print ("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e:  # No more results when next_results doesn't exist
        break
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    #print("This is next results ",next_results)
    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']
    # Show one sample search result by slicing
# Result is printed in JSON format
#print(json.dumps(statuses, indent=1))

status_texts = [ status['text']for status in statuses ]
screen_names = [ user_mention['screen_name']for status in statuses
                    for user_mention in status['entities']['user_mentions']]
hashtags = [ hashtag['text']
for status in statuses
for hashtag in status['entities']['hashtags'] ]
# Compute a collection of all words from all tweets
words = [ w for t in status_texts
                for w in t.split() ]
# Explore the first 5 items for each...
#print (json.dumps(status_texts, indent=1))
print ("Screen Names  ",json.dumps(screen_names, indent=1))
print ("Travel Hashtags   ",json.dumps(hashtags, indent=1))
print (json.dumps(words, indent=1))


for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print (c.most_common()[:20]) # top 10
    print