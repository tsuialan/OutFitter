#!/usr/bin/python

def genUrl():
    url = ""

    with open('keywords.txt') as f:
        data = f.readlines()
    for line in data:
        url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + line
    print(url)
    return url
    f.close()
