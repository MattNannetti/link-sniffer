import os
from flask import Flask


app = Flask(__name__)


from linkSniffer import routes