import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

def login_twitter():
    CONSUMER_KEY = 'QlZUBAbMB9suzDKI1PeVsX4Hk'
    CONSUMER_SECRET = 'qbclbrBtJyP3v22JMZY2plyO2PzyMIJXIqbs1NUjVrFV4HOiO5'
    OAUTH_TOKEN = '781110054284103681-DLx1WVyCzSLCzH0zLYK25cU0A7vLQow'
    OAUTH_TOKEN_SECRET = 'qN0EpBgFNKrpHYmhf47qhODi1vP6g8nVLs7OTAYlkJLq2'
    auth1 = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth1)
    return twitter_api
def login_twitter1():
    CONSUMER_KEY = 'QlZUBAbMB9suzDKI1PeVsX4Hk'
    CONSUMER_SECRET = 'qbclbrBtJyP3v22JMZY2plyO2PzyMIJXIqbs1NUjVrFV4HOiO5'
    OAUTH_TOKEN = '781110054284103681-DLx1WVyCzSLCzH0zLYK25cU0A7vLQow'
    OAUTH_TOKEN_SECRET = 'qN0EpBgFNKrpHYmhf47qhODi1vP6g8nVLs7OTAYlkJLq2'
    auth1 = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.TwitterStream(auth=auth1)
    return twitter_api