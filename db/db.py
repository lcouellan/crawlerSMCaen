# -*-coding:utf-8 -*
from pymongo import MongoClient
import json
import sys
sys.path.insert(0, 'config')
import config #app token, not gitable

def connect(database):
	client = MongoClient('mongodb://'+ config.MONGO_USER +':'+ config.MONGO_PASS +'@mongodb.info.unicaen.fr:27017/')
	db = client[database]
	return db

def insertDB(db,collection,filename):
    col = db[collection]
    data = []
    with open("crawlers/tmp/"+filename) as f:
        for line in f:
            data.append(json.loads(line))
    col.insert(data)

def insertParseDB(db,collection,filename):
	col = db[collection]
	data = []
	with open("parsers/tmp/"+filename) as f:
		for line in f:
			data.append(json.loads(line))
	col.insert(data)

def find(collection, query , colAffichees):
	posts = []
	for post in collection.find( query ):
		posts.append(post)
	return posts

def findAll(collection):
	posts = []
	for post in collection.find():
		posts.append(post)
	return posts

def findTweets(collection):
	posts = []
	for post in collection.find( {} ,{"id_str":1,"text":1} ):
		posts.append(post)
	return posts

def findPosts(collection):
	posts = []
	for post in collection.find( {} ,{"_id":1,"message":1} ):
		posts.append(post)
	return posts


def deleteData(collection):
	collection.delete_many({})

def countCollection(collection):
	return collection.count()

def countReactionPosts(collection, idPost, type):
	compteur = 0
	for post in collection.find( {"id":idPost} ,{"reactions":1} ):
		for k in post["reactions"]["data"]:
			if(k["type"] == type):
				#print (k["type"])
				compteur+=1
	return compteur

def findComments(collection, idPost):
	comments = []
	for post in collection.find( {"id":idPost} ,{"comments":1} ):
		for comment in post["comments"]["data"]:
			comments.append(comment)
	return comments

def findAllComments(collection):
	comments = []
	for post in collection.find( {} ,{"comments":1} ):
		for comment in post["comments"]["data"]:
			comments.append(comment)
	return comments

def countLikeComment(collection, idPost, idComment):
	for post in collection.find( {"id":idPost} ,{"comments":1} ):
		for comment in post["comments"]["data"]:
			if(comment["id"] == idComment):
				return comment["like_count"]