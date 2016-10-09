from pymongo import MongoClient
import json

def insertDB(database,collection,filename):

	client = MongoClient()
	db = client[database]
	col = db[collection]
	data = []
	with open("json/"+filename) as f:
		for line in f:
			data.append(json.loads(line))
	col.insert(data)