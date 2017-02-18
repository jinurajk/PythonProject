import twitter
import json
import TwitterLogin

#This method is used for Twitter login, defined in TwitterPgm3.py
twitter_api = TwitterLogin.login_twitter()

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print (twitter_api.domain)

WORLD_WOE_ID = 1
US_WOE_ID = 90534531
#This is the woeid of Bonn, Germany
DE_WOE_ID = 650272
# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
de_trends = twitter_api.trends.place(_id=DE_WOE_ID)
print (de_trends)
print()

# To dump in JSON format json.dumps and import json
#print (json.dumps(de_trends, indent=1))
print("xxxx",de_trends[0]['trends'])
world_trends_set = set([trend['name']for trend in world_trends[0]['trends']])
de_trends_set = set([trend['url']for trend in de_trends[0]['trends']])
common_trends = world_trends_set.intersection(de_trends_set)
print(world_trends_set)
print(de_trends_set)
print(common_trends)

