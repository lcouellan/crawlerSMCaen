#!/usr/bin/python3
# -*-coding:utf-8 -*

import time
import processCrawlers
import sys
sys.path.insert(0, 'crawlers')
import crawlerMatchNfo
import urllib


date_jour = time.strftime("%Y:%m:%d")
crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
crawling = False

file = open('json/matchNfo.txt', 'r')
for line in file:
    if date_jour == line.split(' - ')[4].strip():
        hashtag = line.split(' - ')[1].strip()
        date_start_crawling = line.split(' - ')[2].strip()
        date_stop_crawling = line.split(' - ')[3].strip()
        crawling = True
        break
file.close()

#crawl automatique:
if crawling:
    processCrawlers.cronCrawlers(hashtag, date_start_crawling, date_stop_crawling)

#craw manuel:
crawl_manuel : False #if turn False after each use
if crawl_manuel:
    hashtag_match = "" # format #SMC/sloganAutreEquipe
    date_start_crawling = "" #format YYYY:MM:DD hh:mm:ss
    date_stop_crawling = "" #format YYYY:MM:DD hh:mm:ss
    processCrawlers.cronCrawlers(hashtag, date_start_crawling, date_stop_crawling)


#TEST LENA
# database = db.connect(config.MONGO_DB)

# db.insertDB(database,"tweets","data_twitter.json")
# db.insertDB(database,"posts","data_facebook.json")
# posts = db.findAll(database["posts"])
# posts = db.find(database["tweets"] , { "text": "RT @SMCaen: Une minute d\'applaudissement est respectée en l\'hommage d\'un supporter décédé, RIP \"Bentek\"! #SMCTFC #SMCaen #TeamSMC #Ligue1" } , {"text":1} )
# posts = db.find(database["tweets"] , {} , {"text":1} )
# for post in posts:
#     print(post)
# db.deleteData(database["tweets"])
# db.deleteData(database["posts"])

# data = urllib.parse.urlencode({ "text": post[0] })
# u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data.encode('ascii'))
# the_page = u.read()
# print (the_page)