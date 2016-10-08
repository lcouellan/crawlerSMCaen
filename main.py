import sys
sys.path.insert(0, 'crawlers')
import crawlerTwitter


crawlerTwitter.crawlTweets('#SMCaen','2016-10-01','2016-10-03','data.json')