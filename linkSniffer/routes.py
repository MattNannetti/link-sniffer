import os
from flask import render_template, url_for, flash, redirect
from linkSniffer.forms import SearchForm
from linkSniffer import app
from bs4 import BeautifulSoup
import requests
import re


#URL = 'http://127.0.0.1:2000/api/v1/ressources/cocktails/all'

@app.route('/')
@app.route('/home')
def home():
    form = SearchForm()

    url = request.args.get('imput_url')

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    soup.find(re.compile('[\w\.-]+@[\w\.-]+\.\w+'))




    return render_template('index.html', form = form)

