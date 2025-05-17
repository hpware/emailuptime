# Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import dotenv
import os
import uuid
from flask import Flask

# Init
app = Flask(__name__)
dotenv.load_dotenv()

# Flask
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gmail")
def gmailStatus():
    return "sys"

@app.route("/outlook")
def outlookStatus():
    return "sys"

@app.route("/yahoo")
def yahooStatus():
    return "sys"

@app.route("/icloud")
def icloudStatus():
    return "sys"

@app.route("/fastmail")
def fastmailStatus():
    return "sys"