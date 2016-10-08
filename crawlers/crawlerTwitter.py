from twitter import *

import json
import sys
sys.path.insert(0, 'config')
import config


def crawlTweets(hashtag,dateD,dateF,filename):
	t = Twitter(
    auth=OAuth(config.TOKEN, config.TOKEN_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET))
	search = t.search.tweets(q=hashtag, since=dateD, until=dateF, count=1000)
	tweets = search['statuses']
	jsonParse = ""
	for tweet in tweets:
		jsonParse = jsonParse +  json.dumps(tweet, sort_keys=True, indent=4)
	fptr = open('json/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()
