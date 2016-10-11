#!/usr/bin/python3
# -*-coding:utf-8 -*

#parsing
# data = urllib.parse.urlencode({ "text": post[0] })
# u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data.encode('ascii'))
# the_page = u.read()
# print (the_page)
    posts = db.find(database["tweets"] , {} , {"text":1} )
