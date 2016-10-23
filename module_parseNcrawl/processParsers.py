#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, '../db')
import db
sys.path.insert(0, '../config')
import config
sys.path.insert(0, 'parsers')
import parser
import shutil
import time
import os

def cronParsers():
    database = db.connect(config.MONGO_DB)
    log = open('logs/cronLogs.txt','a')
    date_jour = time.strftime("%x %X")

    print("\nparser started le " + date_jour)
    log.write("\nparser started le " + date_jour)

    print("parsing new tweets")
    log.write("\nparsing new tweets")
    tweets = db.findTweets(database["tweets_tmp"])
    parser.parseTweets(tweets,"tweets.json") #ligne à remplacer par ajout mongo
    db.insertParseDB(database,"parseTweets","tweets.json")
    db.deleteData(database["tweets_tmp"])

    print("parsing d'un post")
    log.write("\nparsing d'un posts")
    comments = db.findComments(database["posts_tmp"], "237927042913045_1184610918244648")
    parser.parseComments(comments,"post1.json")
    db.insertParseDB(database,"parseComments","post1.json")
    
    print("done.")
    date_jour = time.strftime("%x %X")
    log.write("\nFinishing parsing at " + date_jour + "\n")

    log.close()