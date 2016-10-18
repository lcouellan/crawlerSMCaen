#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, '../db')
import db
import urllib.request
import json

def parse(database):
	posts = db.find(database , {} ,{"_id":1,"text":1})
	jsonParse = ""
	#parsing
	for post in posts:
		data = urllib.parse.urlencode({ "text": post })
		url = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data.encode('ascii'))
		page = url.read().decode()
		str1 = page
		list1 = list(str1)
		id = ', "idTweet": "'+ str(post["_id"]) +'"}'
		list1[-1:] = id
		str1 = ''.join(list1)
		jsonParse += str1 + "\n"
		fptr = open("parsers/tmp/tmp2.json", "w")
		fptr.write(jsonParse)
		fptr.close()