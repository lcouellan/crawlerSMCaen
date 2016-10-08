import sys
sys.path.insert(0, 'crawlers')
import crawlerTwitter
import crawlerFacebook
import crawlerMatchNfo

crawlerTwitter.crawlTweets('#SMCaen','2016-10-01','2016-10-03','data_twitter.json')
crawlerFacebook.crawlFacebook('SMCaen.officiel','2016:09:16 08:00:00','2016:09:17 23:59:59','data_facebook.json')
crawlerMatchNfo.crawlMatchDate('matchNfo.txt')