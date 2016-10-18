#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, '../db')
sys.path.insert(0, '../config')
import config
import crawlerTwitter
import crawlerFacebook
import db
import shutil
import time
import os

def cronCrawlerTwitter(hashtag, date_start_crawling, database, log):
    #transformation des dates pour correspondre au modèle twitter
    date = date_start_crawling.split(' ')[0].split(':')
    date_start_1 = date[0] + "-" + date[1] + "-" + date[2] #n-1
    date_start_2 = date[0] + "-" + date[1] + "-" + "0" + str(int(date[2])+1) #n
    date_start_3 = date[0] + "-" + date[1] + "-" + "0" + str(int(date[2])+2) #n+1
    date_start_4 = date[0] + "-" + date[1] + "-" + "0" + str(int(date[2])+3) #n+1

    #---Crawl du #SMCaen---:
    print("crawling twitter #SMCaen du " + date_start_1 )
    log.write("\ncrawling twitter #SMCaen du " + date_start_1)
    crawlerTwitter.crawlTweets('#SMCaen', date_start_1, date_start_2, 'data_twitter.json')
    if (os.stat("crawlers/tmp/data_twitter.json").st_size != 0):
        print("adding twitter #SMCaen in MongoDb")
        log.write("\nadding twitter #SMCaen in MongoDb")
        db.insertDB(database,"tweets","data_twitter.json")
        db.insertDB(database,"tweets_tmp","data_twitter.json")
    else:
        print("no data from twitter in this period")
        log.write("\nno data from twitter in this period")

    print("crawling twitter #SMCaen du " + date_start_2 )
    log.write("\ncrawling twitter #SMCaen du " + date_start_2)
    crawlerTwitter.crawlTweets('#SMCaen', date_start_2, date_start_3, 'data_twitter.json')
    if (os.stat("crawlers/tmp/data_twitter.json").st_size != 0):
        print("adding twitter #SMCaen in MongoDb")
        log.write("\nadding twitter #SMCaen in MongoDb")
        db.insertDB(database,"tweets","data_twitter.json")
        db.insertDB(database,"tweets_tmp","data_twitter.json")
    else:
        print("no data from twitter in this period")
        log.write("\nno data from twitter in this period")

    print("crawling twitter #SMCaen du " + date_start_3 )
    log.write("\ncrawling twitter #SMCaen du " + date_start_3)
    crawlerTwitter.crawlTweets('#SMCaen', date_start_3, date_start_4, 'data_twitter.json')
    if (os.stat("crawlers/tmp/data_twitter.json").st_size != 0):
        print("adding twitter #SMCaen in MongoDb")
        log.write("\nadding twitter #SMCaen in MongoDb")
        db.insertDB(database,"tweets","data_twitter.json")
        db.insertDB(database,"tweets_tmp","data_twitter.json")
    else:
        print("no data from twitter in this period")
        log.write("\nno data from twitter in this period")

    #---Crawl du #match---:
    print("crawling twitter" + hashtag + " du " + date_start_2 )
    log.write("\ncrawling twitter" + hashtag + " du " + date_start_2)
    crawlerTwitter.crawTweetsWithoutDate(hashtag, 'data_twitter.json')
    if (os.stat("crawlers/tmp/data_twitter.json").st_size != 0):
        print("adding twitter " + hashtag + " in MongoDb")
        log.write("\nadding twitter " + hashtag + " in MongoDb")
        db.insertDB(database,"tweets","data_twitter.json")
        db.insertDB(database,"tweets_tmp","data_twitter.json")
    else:
        print("no data from twitter in this period")
        log.write("\nno data from twitter in this period")

def cronCrawlers(hashtag, date_start_crawling, date_stop_crawling):
    database = db.connect(config.MONGO_DB)
    log = open('crawlers/logs/cronLogs.txt','a')
    log.write("\n------------------------")
    date_jour = time.strftime("%x %X")

    print("crawler started le " + date_jour)
    log.write("\ncrawler started le " + date_jour)
    cronCrawlerTwitter(hashtag, date_start_crawling, database, log)
    
    print("crawling post SMCaen.officiel")
    log.write("\ncrawling post SMCaen.officiel")
    crawlerFacebook.crawlFacebook('SMCaen.officiel', date_start_crawling, date_stop_crawling, 'data_facebook.json')
    print("adding post SMCaen.officiel in MongoDb")
    log.write("\nadding post SMCaen.officiel in MongoDb")
    db.insertDB(database,"posts","data_facebook.json")
    db.insertDB(database,"posts_tmp","data_facebook.json")
    print("done.")
    date_jour = time.strftime("%x %X")
    log.write("\nFinishing crawling at " + date_jour + "\n")

    log.close()