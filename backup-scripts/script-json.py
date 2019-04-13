#!/usr/bin/python

dataLog = []

keyOne = '"description": '
keyTwo = '"label": '

with open('response.txt') as f:
    data = f.readlines()
for line in data:
    if line.__contains__(keyOne):
        line = line.replace(keyOne,'')
        line = line.replace('"','')
        line = line.replace(',','')
        line = line.replace(' ','')
        line = line.rstrip()
        print(line, end = '')
        dataLog.append(line)
    if line.__contains__(keyTwo):
        line = line.replace(keyTwo,'')
        line = line.replace('"','')
        line = line.replace(',','')
        line = line.replace(' ','')
        line = line.rstrip()
        print(line, end = '')
        dataLog.append(line)

kwString = ""
nf = open("keywords.txt", "w")
for word in dataLog:
    kwString += word + "+"
nf.write(kwString)
nf.close()
