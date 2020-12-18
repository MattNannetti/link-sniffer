import os
from flask import Flask


app = Flask(__name__)


app.config['SECRET_KEY'] = '54cb0a1257b1585952f7ea15492dc6fa'


from linkSniffer import routes