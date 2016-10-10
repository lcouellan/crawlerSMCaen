from pymongo import MongoClient
import json
import sys
sys.path.insert(0, 'config')
import config #app token, not gitable

def insertDB(database,collection,filename):

    client = MongoClient('mongodb://'+ config.MONGO_USER +':'+ config.MONGO_PASS +'@mongodb.info.unicaen.fr:27017/')
    db = client[database]
    col = db[collection]
    data = []
    with open("json/"+filename) as f:
        for line in f:
            data.append(json.loads(line))
    col.insert(data)
