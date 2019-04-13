#!/usr/bin/python
from flask import Flask, render_template, redirect
import os
import script_console
import script_json
import script_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/script/')
def index2():
    script_console.runJSonScript()
    script_json.genKeywords()
    url = script_url.genUrl()
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
