# crawlerSMCaen
First part of a Web project for collecting and parsing reactions from social networks (Facebook and Twitter). The analysis is focused on suporter feeling of the soccer team Stade Malherbe de Caen.

It's a group project involving Lénaïc Couellan and Pierre Labadille, students in M2-DNR2i from the University of Caen.

## Installing

Clone the repository (localy or in python server)
```
git clone https://github.com/lcouellan/crawlerSMCaen.git
cd crawlerSMCaen
```

Rename the file "config_template.py" to "config.py" and fill it with your MongoDb id (locate in: /config/)

Run installDependencies.sh to install dependencies
```
chmod +x installDependencies.sh
sudo ./installDependencies.sh
```

Set up a CRONTAB to automate the parser and crawler
```
crontab -e
#[end of file add]:
#replace ~ by your path
#replace 3 to set the hour of the day you wish
0 3 * * * cd ~/crawlerSMCaen/module_parseNcrawl/ && python3 main.py
```

## Important note

The second part of the project (search engine and feelings monitoring) is available: [`feelingAnalysisSMCaen`](https://github.com/plabadille/feelingAnalysisSMCaen).

## Built with

* [`Facebook API Graph`](https://developers.facebook.com/docs/graph-api/)
* [`Twitter API Search`](https://dev.twitter.com/rest/public/search)
* [`Text Processing Sentiment Analysis`](http://text-processing.com/docs/sentiment.html)
* [`Python3`](https://www.python.org/download/releases/3.0/)
* [`MongoDb`](https://www.mongodb.com/fr)

## License

This project is licensed under the GNU License - see the [LICENCE](LICENSE) file for details
