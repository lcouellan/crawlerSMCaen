#!/usr/bin/python3 
# -*-coding:utf-8 -*

import sys
sys.path.insert(0, '../config')
import config #app token, not gitable
import json #json
import re #regex
import requests #urllib.request amélioré (non suffisant pour ce genre de requête)


def crawlFacebook(page_id,start_parsing_date,end_parsing_date,filename):
    #1- préparation de la requête
    token_app = config.APP_ID + "|" + config.APP_SECRET_KEY
    api_url = "https://graph.facebook.com/v2.8/"
    query = "/?fields=posts.since(" + start_parsing_date + ").until(" + end_parsing_date + "){comments.limit(1500){message.limit(1500),like_count,created_time},reactions.limit(1500),message,created_time}&access_token="
    fb_graph_url = api_url + page_id + query + token_app
    responseStr = requests.get(fb_graph_url).text

    #2- mise en forme du json de sortie
    jsonParse = re.sub('{"posts":{"data":\[', '', responseStr) #on supprime le conteneur global qui ne nous interesse pas
    jsonParse = re.sub(',"paging":{"cursors":{"before":"\w*","after":"\w*"}}', '', jsonParse) #on suprime les pagers (vide)
    jsonParse = re.sub('],"paging":{"previous":.*$', '', jsonParse) #fermeture du conteneur global et pager global
    jsonParse = re.sub('}]}},', '}]}}\n', jsonParse) #un post par ligne

    fptr = open('crawlers/tmp/'+filename, "w")
    fptr.write(jsonParse)
    fptr.close()

    #3- archivage:
    date = start_parsing_date.split(' ')[0].split(':')
    dateD = date[0] + "-" + date[1] + "-" + date[2]
    filename = dateD  + "_crawlPosts_" + page_id + ".json"
    fptr = open('json/'+filename, "w")
    fptr.write(jsonParse)
    fptr.close()