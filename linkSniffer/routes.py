import os
from flask import render_template, url_for, flash, redirect
from linkSniffer.forms import SearchForm
from linkSniffer import app
from bs4 import BeautifulSoup
import requests
import re


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()

    url = form.urlInput.data

    if url:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        # regex email
        email_list = []
        for email in soup.find_all(string=re.compile("[\w\.-]+@[\w\.-]+\.\w+")):
            email_list.append(email)


        # url href
        link_list = []
        for a in soup.find_all("a"):
            try:
                link_list.append(a['href'])
            except Exception as e:
                pass

        for area in soup.find_all("area"):
            try:
                link_list.append(area['href'])
            except Exception as e:
                pass

        for base in soup.find_all("base"):
            try:
                link_list.append(base['href'])
            except Exception as e:
                pass

        for link in soup.find_all("link"):
            try:
                link_list.append(link['href'])
            except Exception as e:
                pass

        results  = []
        results.append(email_list)
        results.append(link_list)
        print(results)
        return render_template('index.html', form=form, results=results)
    else:
        return render_template('index.html', form=form)
