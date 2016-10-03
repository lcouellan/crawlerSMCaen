from twitter import *
import json
import urllib2


TOKEN = "762391442-y2wNnNRtE8iU2A7qFaYFs0dtzFy04UvRYUbghAHK"
TOKEN_SECRET = "YF5MoH9QntVnB1zDJEaMlVVjGyOAZYWxJ7HgEjnZbDsiA"
CONSUMER_KEY = "3tep17sg2gYJKLrgcmkELweaH"
CONSUMER_SECRET = "gBXF13bVAWbUpdV2d7G8e3t9qv4tneXsck1qn4R7HUuEgLYAOy"




def crawlTweets(hashtag,dateD,dateF,filename):
	t = Twitter(
    auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
	search = t.search.tweets(q=hashtag, since=dateD, until=dateF, count=1000)
	tweets = search['statuses']
	jsonParse = ""
	for tweet in tweets:
		jsonParse = jsonParse +  json.dumps(tweet, sort_keys=True, indent=4)
	fptr = open('json/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()

crawlTweets('#SMCaen','2016-10-01','2016-10-03','data.json')