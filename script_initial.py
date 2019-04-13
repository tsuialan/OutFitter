#!/usr/bin/python

from flask import Flask, request, json

if request.method == 'POST':
	url = request.form['url']
