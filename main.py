#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, 'db')
sys.path.insert(0, 'config')
import config
import crawlerTwitter
import crawlerFacebook
import crawlerMatchNfo
import db
<<<<<<< Updated upstream
import shutil

crawlerTwitter.crawlTweets('#SMCaen','2016-10-01','2016-10-03','data_twitter.json')
crawlerFacebook.crawlFacebook('SMCaen.officiel','2016:09:16 08:00:00','2016:09:17 23:59:59','data_facebook.json')
crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
db.insertDB(config.MONGO_DB,"tweets","data_twitter.json")
db.insertDB(config.MONGO_DB,"posts","data_facebook.json")
shutil.rmtree("json/")
=======
import time

print (time.strftime("%Y:%m:%d"))
crawlerMatchNfo.crawlMatchDate('matchNfo.txt') #on actualise le fichier de date

# crawlerTwitter.crawlTweets('#SMCaen','2016-10-01','2016-10-03','data_twitter.json')
crawlerFacebook.crawlFacebook('SMCaen.officiel','2016:09:16 08:00:00','2016:09:17 23:59:59','data_facebook.json')
# crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
# db.insertDB(config.MONGO_DB,"tweets","data_twitter.json")
# db.insertDB(config.MONGO_DB,"posts","data_facebook.json")
>>>>>>> Stashed changes
