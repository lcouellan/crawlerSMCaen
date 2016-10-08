#!/usr/bin/python3

#crawl calendrier sm caen
#page crawlé: http://www.smcaen.fr/calendrier-resultat/2016-2017/premiere/complet

import urllib.request
import json
import re #regex

def cleanhtml(raw_html): #fonction pour retirer les balises html
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def frenchMonthInNumber(x): #retourne le numéro de mois
    return {
        'janvier': "01",
        'février': "02",
        'mars': "03",
        'avril': "04",
        'mai': "05",
        'juin': "06",
        'juillet': "07",
        'août': "08",
        'septembre': "09",
        'octobre': "10",
        'novembre': "11",
        'décembre': "12"
    }[x]

def sigle(x): #retourne le sigle d'une équipe
    return {
        'Nice': "OGCN",
        'Monaco': "ASM",
        'Paris SG': "PSG",
        'Toulouse': "TFC",
        'Lyon': "OL",
        'Bordeaux': "FCGB",
        'Rennes': "SRFC",
        'FC Metz': "FCM",
        'Saint-Etienne': "ASSE",
        'Guingamp': "EAG",
        'Bastia': "SCB",
        'Angers': "SCO",
        'SM Caen': "SMC",
        'Marseille': "OM",
        'Dijon FCO': "DFCO",
        'Nantes': "FCN",
        'Montpellier': "MHSC",
        'Lille': "LOSC",
        'Lorient': "FCL",
        'AS Nancy': "ASNL"
    }[x]

def crawlMatchDate(filename):
    #on reccup la page complète:
    fp = urllib.request.urlopen("http://www.smcaen.fr/calendrier-resultat/2016-2017/premiere/complet")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    #on l'explode en ligne:
    split_mystr = mystr.splitlines()
    #on supprime tout ce qui ce trouve avant le début du tableau (REGEX multiligne bien trop lent):
    i = 0
    for line in split_mystr:
        if re.search('<table id="cal-res">', line):
            break
        i += 1
    del split_mystr[:i]

    #on supprime tout ce qui ce trouve après le début du tableau:
    i = 0
    for line in split_mystr:
        if re.search('</table>', line):
            i += 1
            break
        i += 1
    del split_mystr[i:]

    #on sépare chaque mois:
    start_line_month = []
    i = 0
    for line in split_mystr:
        if re.search('<span class="date">', line):
            start_line_month.append(i)
        i +=1

    i = 1
    content_month = {}
    for start_line in start_line_month:
        content_month[i] = []
        if i == len(start_line_month): #pour le dernier mois on prend la dernière ligne
            end_line = len(split_mystr)
        else: #sinon on prend la ligne de début du mois suivant - 1
            end_line = start_line_month[i] - 1

        x = start_line
        while x < end_line:
            content_month[i].append(split_mystr[x])
            x += 1        
        i += 1

    #on sépare chaque match dans chaque mois:
    month = {}
    for key in content_month.keys():
        month[key] = {}
        start_line_match = []
        i = 0
        for line in content_month[key]:
            if re.search('<tr class="tr-cr', line):
                start_line_match.append(i)
            i +=1

        i = 1
        for start_line in start_line_match:
            month[key][i] = []
            if i == len(start_line_match):
                end_line = len(content_month[key])
            else:
                end_line = start_line_match[i] - 1

            x = start_line
            while x < end_line:
                month[key][i].append(content_month[key][x])
                x += 1        
            i += 1

    #on met en forme les données que l'on veut conserver:
    line_to_write = "";
    for key in content_month.keys():
        real_month = frenchMonthInNumber(cleanhtml(content_month[key][1]).strip())
        year = cleanhtml(content_month[key][2]).strip()
        for key2 in month[key].keys():
            if key2 != len(month[key]):
                day = cleanhtml(month[key][key2][4]).strip()
                interieur = sigle(cleanhtml(month[key][key2][12]).strip())
                exterieur = sigle(cleanhtml(month[key][key2][19]).strip())
                if interieur == "SMC":
                    hashtag = "#" + interieur + "/" + exterieur
                else:
                    hashtag = "#" + exterieur + "/" + interieur
                date_match = year + ":" + real_month + ":" + day
                date_start_crawling = year + ":" + real_month + ":" + str(int(day) - 1) + " 04:00:00"
                date_stop_crawling = year + ":" + real_month + ":" + str(int(day) + 1) + " 23:59:59"
                
                line_to_write += date_match + " - " + hashtag + " - " + date_start_crawling + " - " + date_stop_crawling + "\n"

    #on stock le tout dans un fichier:
    fptr = open('json/'+filename, "w")
    fptr.write(line_to_write)
    fptr.close()