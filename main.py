#!/usr/bin/python3 
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, 'db')
import crawlerTwitter
import crawlerFacebook
import crawlerMatchNfo
import db

#crawlerTwitter.crawlTweets('#SMCaen','2016-10-01','2016-10-03','data_twitter.json')
#crawlerFacebook.crawlFacebook('SMCaen.officiel','2016:09:16 08:00:00','2016:09:17 23:59:59','data_facebook.json')
#crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
db.insertDB("crawlSMCaen","tweets","data_twitter.json")