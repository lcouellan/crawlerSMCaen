#!/usr/bin/python3
# -*-coding:utf-8 -*

from twitter import *

import json
import sys
sys.path.insert(0, '../config')
import config
import re


def crawlTweets(hashtag,dateD,dateF,filename):
	t = Twitter(
    auth=OAuth(config.TOKEN, config.TOKEN_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET))
	search = t.search.tweets(q=hashtag, since=dateD, until=dateF, count=1000)
	tweets = search['statuses']
	jsonParse = ""
	for tweet in tweets:
		jsonParse = jsonParse +  json.dumps(tweet) + "\n"
	fptr = open('crawlers/tmp/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()

	#archivage:
	if re.search('/', hashtag):
		hashtag = hashtag.split('/')[0] + "-" + hashtag.split('/')[1]
	filename = dateD  + "_crawl_" + hashtag + ".json"
	fptr = open('json/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()

def crawTweetsWithoutDate(hashtag, filename):
	t = Twitter(
    auth=OAuth(config.TOKEN, config.TOKEN_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET))
	search = t.search.tweets(q=hashtag, count=1000)
	tweets = search['statuses']
	jsonParse = ""
	for tweet in tweets:
		jsonParse = jsonParse +  json.dumps(tweet) + "\n"
	fptr = open('crawlers/tmp/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()

	#archivage:
	if re.search('/', hashtag):
		hashtag = hashtag.split('/')[0] + "-" + hashtag.split('/')[1]
	filename = "match_crawl_" + hashtag + ".json"
	fptr = open('json/'+filename, "w")
	fptr.write(jsonParse)
	fptr.close()