import os
from flask import render_template, url_for, flash, redirect
from linkSniffer import app


#URL = 'http://127.0.0.1:2000/api/v1/ressources/cocktails/all'
#price = str(requests.request("GET", url, headers=headers, params = querystring).json()['Quotes'][0]['MinPrice'])

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')