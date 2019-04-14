#!/usr/bin/python

import os
from pathlib import Path

def genResponse():
    os.system("curl -v -s -H 'Content-Type: application/json' \
        https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCgYLR6tIgUSpuNyTadxfuLadPDXSLP8OI \
        --data-binary @requestw.json > responsew.txt");

def genKeywords():
    dataLog = []

    keyOne = '"description": '
    keyTwo = '"label": '

    config = Path('responsew.txt')
    if config.is_file():
        print()
    else:
        genResponse()

    with open('responsew.txt') as f:
        data = f.readlines()
    for line in data:
        if line.__contains__(keyOne):
            line = line.replace(keyOne,'')
            line = line.replace('"','')
            line = line.replace(',','')
            line = line.replace(' ','')
            line = line.rstrip()
            #print(line, end = '')
            dataLog.append(line)
        if line.__contains__(keyTwo):
            line = line.replace(keyTwo,'')
            line = line.replace('"','')
            line = line.replace(',','')
            line = line.replace(' ','')
            line = line.rstrip()
            #print(line, end = '')
            dataLog.append(line)

    kwString = ""
    nf = open("keywordsw.txt", "w")
    for word in dataLog:
        kwString += word + "+"
    nf.write(kwString)
    nf.close()
    return dataLog

def genUrl():
    url = ""

    with open('keywordsw.txt') as f:
        data = f.readlines()
    for line in data:
        url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + line
    print(url)
    return url
    f.close()
