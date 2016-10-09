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
    
    #on supprime les pagers (useless on réccupère toute la data)
    del page["posts"]["paging"]
    for comments in page["posts"]["data"]:
        del comments["comments"]["paging"]
        del comments["reactions"]["paging"]
            
    #print(page)
    jsonParse = json.dumps(page, sort_keys=True, indent=4)
    fptr = open('json/'+filename, "w")
    fptr.write(jsonParse)
    fptr.close()