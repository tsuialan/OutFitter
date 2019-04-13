#!/usr/bin/python

import os

def runJSonScript():
    os.system("curl -v -s -H 'Content-Type: application/json' \
        https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCgYLR6tIgUSpuNyTadxfuLadPDXSLP8OI \
        --data-binary @request.json > response.txt");
