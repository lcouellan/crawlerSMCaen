#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, 'db')
sys.path.insert(0, 'config')
import config
import crawlerTwitter
import crawlerFacebook
import db
import shutil
import time
import os

def cronCrawlers(hashtag, date_start_crawling, date_stop_crawling):
    print("crawling twitter #SMCaen")
    crawlerTwitter.crawlTweets('#SMCaen', date_start_crawling, date_stop_crawling, 'data_twitter.json')
    if (os.stat("json/data_twitter.json").st_size != 0):
        print("adding twitter #SMCaen in MongoDb")
        db.insertDB(config.MONGO_DB,"tweets","data_twitter.json")
    else:
        print("no data from twitter in this period")

    print("crawling twitter " + hashtag)
    crawlerTwitter.crawlTweets(hashtag, date_start_crawling, date_stop_crawling, 'data_twitter.json')
    if (os.stat("json/data_twitter.json").st_size != 0):
        print("adding twitter " + hashtag + " in MongoDb")
        db.insertDB(config.MONGO_DB,"tweets","data_twitter.json")
    else:
        print("no data from twitter in this period")
    
    print("crawling post SMCaen.officiel")
    crawlerFacebook.crawlFacebook('SMCaen.officiel', date_start_crawling, date_stop_crawling, 'data_facebook.json')
    print("adding post SMCaen.officiel in MongoDb")
    db.insertDB(config.MONGO_DB,"posts","data_facebook.json")
    print("done.")    