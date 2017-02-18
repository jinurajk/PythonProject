import json
import TwitterLogin
import twitter
twitter_api = TwitterLogin.login_twitter()
#twitter_api = twitter.Twitter(domain='api.twitter.com', api_version='1')
print(json.dumps(twitter_api.trends(), indent=1))