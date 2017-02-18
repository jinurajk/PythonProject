#This programs is for retrieving all tweets from a particular user

import json
import TwitterLogin
import os
import codecs
from collections import Counter


#This method is used for Twitter login, defined in TwitterPgm3.py
twitter_api = TwitterLogin.login_twitter()
#twitter_api.direct_messages.new(user="StillIbok",text="I think I am working!")

#jinuraj = json.dumps(twitter_api.statuses.user_timeline(screen_name="k_jinuraj"))
#print(jinuraj)


def method_getalltweets(name):
    name = name
    num = 0
    lis = []
    #alltweets = []
    fo = codecs.open("princetweets.txt", "w+", 'utf-8')
    user_timeline = twitter_api.statuses.user_timeline(screen_name=name, count=1)
    for tweet in user_timeline:
        lis.append(tweet['id'])
    print ("List -us 1" ,lis[-1])

    max_id = []
    for i in range(0, 17): ## iterate through 16 times to get max No. of tweets
        user_timeline = twitter_api.statuses.user_timeline(screen_name=name,count=200,max_id=lis[-1])
    #user_timeline = twitter_api.search.tweets(screen_name="StillIbok", count=200)
    #print(user_timeline)
        for tweet in user_timeline:
            num = num + 1
            print (num, tweet['text'], tweet['id'])
            str1 = tweet['text']
            #str1.append(num)
            fo.write(str(num))
            fo.write(str1)
            lis.pop()
            lis.append(tweet['id'])
        #print("Listttttt", lis)

    fo.close()


method_getalltweets("StillIbok")
#method_getalltweets("@LufthansaLatina")
#method_getalltweets("nabu_xavier")
