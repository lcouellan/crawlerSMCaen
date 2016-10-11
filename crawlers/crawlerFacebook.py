 #!/usr/bin/python3 
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, 'config')
import config #app token, not gitable
import facebook #facebook-sdk
import json #json
import re #regex

def crawlFacebook(page_id,start_parsing_date,end_parsing_date,filename):
    token_app = config.APP_ID + "|" + config.APP_SECRET_KEY #doit être renseigné dans un fichier config.py
    graph = facebook.GraphAPI(access_token=token_app, version='2.7')
    
    #query for all scale of comments: {message, comments.limit(1500){message.limit(1500), reactions.limit(1500), comments.limit(1500){message.limit(1500)}}, reactions.limit(1500)}
    #query for post, comments and reaction (firstLevel&secondLevel)
    query = "{message, comments.limit(1500){message.limit(1500), reactions.limit(1500)}, reactions.limit(1500)}"

    page = graph.get_object(id=page_id, fields='posts.since(' + start_parsing_date + ').until(' + end_parsing_date + ')' + query)
               
    jsonParse = json.dumps(page) + "\n"
    fptr = open('crawlers/tmp/'+filename, "w")
    fptr.write(jsonParse)
    fptr.close()

    #archivage:
    date = start_parsing_date.split(' ')[0].split(':')
    dateD = date[0] + "-" + date[1] + "-" + date[2]
    filename = dateD  + "_crawlPosts_" + page_id + ".json"
    fptr = open('json/'+filename, "w")
    fptr.write(jsonParse)
    fptr.close()