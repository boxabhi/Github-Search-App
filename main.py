from flask import Flask,render_template,request, session, flash,redirect,url_for,session,redirect
import json
from datetime import datetime 
import math
import os
import requests


app = Flask(__name__)
app.secret_key = 'hello'

API_URL = 'https://api.github.com/search/users?q={}'



def query_api(search):
	try:
		data = requests.get(API_URL.format(search)).json()
	except Exception as exc:
		data = None
	return data


@app.route('/', methods=['GET','POST'])
def index():
	data = []
	title = 'Github Profile Searcher'
	if (request.method == 'POST'):
		search = request.form.get('username')
		result = query_api(search)
		if result:
			data.append(result)
		return render_template('result.html', data = result)
	return render_template('index.html', title=title )
	


app.run(debug=True)