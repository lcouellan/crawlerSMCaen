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
    processParsers.cronParsers()

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
    #print(db.find(database["tweets"] , { '_id': ObjectId("58061dac6d3a165bf1c1fbb6") } , { "_id":1 , "text":1 } ))
    #fonction de supression
    #db.deleteData(database["tweets"])
    #db.deleteData(database["posts"])
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
    