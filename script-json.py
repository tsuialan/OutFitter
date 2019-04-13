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
        print(line, end = '')
        dataLog.append(line)
    if line.__contains__(keyTwo):
        line = line.replace(keyTwo,'')
        line = line.replace('"','')
        line = line.replace(',','')
        print(line, end = '')
        dataLog.append(line)
