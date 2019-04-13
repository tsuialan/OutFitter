#!/usr/bin/python

import json

def init():
    with open("request.json", "r+ ") as f:
        data = json.load(f)
        print("Before:", data)
        data["requests"][0]["image"]["source"] = "https://i.imgur.com/hJVW9nJ.jpg"
        print("After: ", data)
    f.close()
