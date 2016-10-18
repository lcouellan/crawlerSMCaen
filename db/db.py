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


def find(collection, query , colAffichees):
	posts = []
	for post in collection.find( query , colAffichees ):
		posts.append(post)
	return posts

def findAll(collection):
	posts = []
	for post in collection.find():
		posts.append(post)
	return posts
	
def findTweets(collection):
	posts = []
	for post in collection.find({} ,{"_id":1,"text":1} ):
		posts.append(post)
	return posts


def deleteData(collection):
	collection.delete_many({})

def countCollection(collection):
	return collection.count()