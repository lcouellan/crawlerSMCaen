#!/usr/bin/python3
# -*-coding:utf-8 -*

import time
import processCrawlers
import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, 'parsers')
sys.path.insert(0, '../db')
import db
sys.path.insert(0, '../config')
import config
import parser
import crawlerMatchNfo

date_jour = time.strftime("%Y:%m:%d")
crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
crawling = False

file = open('crawlers/tmp/matchNfo.txt', 'r')
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

#craw manuel (test):
crawl_manuel = False #if turn False after each use
if crawl_manuel:
    hashtag_match = "#MHSCSMC" # format #SMC/sloganAutreEquipe
    date_start_crawling = "2016:10:14 04:00:00" #format YYYY:MM:DD hh:mm:ss
    date_stop_crawling = "2016:10:16 23:59:59" #format YYYY:MM:DD hh:mm:ss
    processCrawlers.cronCrawlers(hashtag_match, date_start_crawling, date_stop_crawling)


#ajoutBdd (test):
add_bd_manuel = False #if turn False after each use
if add_bd_manuel:
    database = db.connect(config.MONGO_DB) #connection à la bdd
    #fonction insertion
    # db.insertDB(database,"tweets","data_twitter.json")
    # #fonction reccupérer toute les data d'une collection
    # posts = db.findAll(database["posts"])
    # #fonction reccupérer selon critères
    # posts = db.find(database["tweets"] , { "text": "RT @SMCaen: Une minute d\'applaudissement est respectée en l\'hommage d\'un supporter décédé, RIP \"Bentek\"! #SMCTFC #SMCaen #TeamSMC #Ligue1" } , {"text":1} )
    # parser.parse(database["tweets"])
    #fonction de supression
    db.deleteData(database["tweets"])
    db.deleteData(database["posts"])