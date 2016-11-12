#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, '../db')
import db
import urllib.request
import json

def parseTweets(tweets,filename):
	#parsing
	jsonParse = ""
	for tweet in tweets:
		data = urllib.parse.urlencode({ "text": tweet })
		url = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data.encode('ascii'))
		page = url.read().decode()
		str1 = page
		list1 = list(str1)
		id = ', "idTweet": "'+ str(tweet["id_str"]) +'"}'
		list1[-1:] = id
		str1 = ''.join(list1)
		jsonParse += str1 + "\n"
		fptr = open("parsers/tmp/"+filename, "w")
		fptr.write(jsonParse)
		fptr.close()

def parseComments(comments,filename):
	#parsing
	jsonParse = ""
	for comment in comments:
		data = urllib.parse.urlencode({ "text": comment })
		url = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data.encode('ascii'))
		page = url.read().decode()
		str1 = page
		list1 = list(str1)
		id = ', "idComment": "'+ str(comment["id"]) +'"}'
		list1[-1:] = id
		str1 = ''.join(list1)
		jsonParse += str1 + "\n"
		fptr = open("parsers/tmp/"+filename, "w")
		fptr.write(jsonParse)
		fptr.close()
