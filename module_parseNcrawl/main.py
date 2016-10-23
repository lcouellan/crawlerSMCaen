#!/usr/bin/python3
# -*-coding:utf-8 -*
from bson.objectid import ObjectId  
import time
import processCrawlers
import processParsers
import sys
sys.path.insert(0, 'crawlers')
sys.path.insert(0, 'parsers')
sys.path.insert(0, '../db')
import db
sys.path.insert(0, '../config')
import config
import parser
import crawlerMatchNfo

crawling = False #let always false, SMCaen crawler will turn in True if needed.
#turn False after each use (for testing):
crawl_manuel = False #testing crawler&parser manualy
#turn False after each use (for testing):
add_bd_manuel = False #testing fonctionality concerning bdd

#log init
log = open('logs/cronLogs.txt','a')
log.write("\n------------------------")
date_jour = time.strftime("%x %X")

#crawl automatique:
if not crawl_manuel:
    #log launching:
    print("script started by cron le " + date_jour)
    log.write("\nscript started by cron le " + date_jour + "\n")
    #crawl SMCaen for fresh date:
    date_jour = time.strftime("%Y:%m:%d")
    crawlerMatchNfo.crawlMatchDate('matchNfo.txt')
    #Check if date match:
    file = open('crawlers/tmp/matchNfo.txt', 'r')
    for line in file:
        if date_jour == line.split(' - ')[4].strip():
            hashtag = line.split(' - ')[1].strip()
            date_start_crawling = line.split(' - ')[2].strip()
            date_stop_crawling = line.split(' - ')[3].strip()
            crawling = True
            break
    file.close()
    #if the date match we process crawlers/parsers:
    if crawling:
        log.close()
        processCrawlers.cronCrawlers(hashtag, date_start_crawling, date_stop_crawling)
        processParsers.cronParsers()
    else:
        print("No automatic crawling/parsing needed")
        log.write("\nNo automatic crawling/parsing needed\n")
        log.close()
else: #manuel launch for testing
    #craw manuel (test):
    if crawl_manuel:
        #log:
        print("script manualy started le " + date_jour)
        log.write("\nscript manualy started le " + date_jour + "\n")
        log.close()
        #Change parameter as needed:
        hashtag_match = "#MHSCSMC" # format #SMC/sloganAutreEquipe
        date_start_crawling = "2016:10:14 04:00:00" #format YYYY:MM:DD hh:mm:ss
        date_stop_crawling = "2016:10:16 23:59:59" #format YYYY:MM:DD hh:mm:ss
        #launch crawlers and parsers:
        processCrawlers.cronCrawlers(hashtag_match, date_start_crawling, date_stop_crawling)
        processParsers.cronParsers()

    #Db fonction for testing (uncomment the uneeded one): 
    if add_bd_manuel:
        database = db.connect(config.MONGO_DB) #connection à la bdd
        #fonction insertion
        # db.insertDB(database,"tweets","data_twitter.json")
        # #fonction reccupérer toute les data d'une collection
        # posts = db.findAll(database["posts"])
        # #fonction reccupérer selon critères
        # posts = db.find(database["tweets"] , { "text": "RT @SMCaen: Une minute d\'applaudissement est respectée en l\'hommage d\'un supporter décédé, RIP \"Bentek\"! #SMCTFC #SMCaen #TeamSMC #Ligue1" } , {"text":1} )
        # parser.parse(database["tweets"])
        #print(db.find(database["tweets"] , { '_id': ObjectId("58061dac6d3a165bf1c1fbb6") } , { "_id":1 , "text":1 } ))
        #Parsing des tweets à partir de Mongo
        #tweets = db.findTweets(database["tweets"])
        #print(tweets)
        # parser.parseTweets(tweets,"test.json")
        #Affichage des posts (id / messages) à partir de Mongo
        # posts = db.findPosts(database["posts"])
        # print(posts)
        # Compte le nombre de posts 
        # print(db.countCollection(database["posts"]))
        # Compte le nombre de réactions pour un post
        #print(db.countReactionPosts(database["posts"], "237927042913045_1184610918244648", "ANGRY"))
        # Donne les commentaires pour chaque post
        #print(db.findComments(database["posts"], "237927042913045_1184610918244648"))
        # Parsing des commentaires FB d'un post à partir de Mongo
        #comments = db.findComments(database["posts"], "237927042913045_1184610918244648")
        #parser.parseComments(comments,"post1.json")
        # Compte le nombre de likes pour un commentaire
        # print(db.countLikeComment(database["posts"], "237927042913045_1184610918244648", "1184610918244648_1184977031541370"))
        
        #fonction de supression
        db.deleteData(database["tweets"])
        db.deleteData(database["posts"])

#log terminated:
print("The task was successfully executed")
log = open('logs/cronLogs.txt','a')
log.write("\n--- The task was successfully executed ---\n")
log.close()