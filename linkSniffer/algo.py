from bs4 import BeautifulSoup
from termcolor import cprint
import requests
import re

url = 'https://gist.github.com/gruber/8891611'

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')


'''
link = soup.find(string=re.compile(""))

for email in soup.find_all(string=re.compile("[\w\.-]+@[\w\.-]+\.\w+")):
    print(email)
    print()
#print(link)
'''

'''
balise holding href :
    <a>
    <area>
    <base>
    <link>
'''

for a in soup.find_all("a"):
    try:
        a_href = a['href']
    except Exception as e:
        a_href = None
    cprint(a_href, 'red')

for area in soup.find_all("area"):
    try:
        area_href = area['href']
    except Exception as e:
        area_href = None
    cprint(area_href, 'green')

for base in soup.find_all("base"):
    try:
        base_href = base['href']
    except Exception as e:
        base_href = None
    cprint(base_href, 'yellow')

for link in soup.find_all("link"):
    try:
        link_href = link['href']
    except Exception as e:
        link_href = None
    cprint(link_href, 'blue')

