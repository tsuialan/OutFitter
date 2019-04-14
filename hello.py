#!/usr/bin/python
from flask import Flask, render_template, redirect, request
import os
import scripts
import scriptsw
import scripts_download
import scripts_downloadw

app = Flask(__name__)

@app.route('/')
def home():
    #script_initial.initUrl()
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/account')
def account():
    return render_template('scriptForm/index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/quiz')
def personQuiz():
    return render_template('Quiz/Example/personality.html')

@app.route('/script/')
def index2():
    scripts.genResponse()
    scripts.genKeywords()
    scripts_download.main()
    #url = scripts.genUrl()
    url = "http://photo-albums-20190413200901-hostingbucket-master.s3-website-us-east-1.amazonaws.com/albums/57dc6292-82ca-4616-9ca6-3d9f6839bfd0"
    return redirect(url, code=302)

@app.route('/account2/')
def account2():
    return render_template('scriptForm/index2.html')

@app.route('/script2/')
def index3():
    scriptsw.genResponse()
    scriptsw.genKeywords()
    scripts_downloadw.main()
    #url = scripts.genUrl()
    url = "http://photo-albums-20190413200901-hostingbucket-master.s3-website-us-east-1.amazonaws.com/albums/57dc6292-82ca-4616-9ca6-3d9f6839bfd0"
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
