#!/usr/bin/python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/script/')
def index2():
    os.system("curl -v -s -H 'Content-Type: application/json' \
        https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCgYLR6tIgUSpuNyTadxfuLadPDXSLP8OI \
        --data-binary @request.json > response.json");
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
