# Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import dotenv
import os
import uuid
from flask import Flask
from providers.gmail import get_gmail_status
from providers.fastmail import get_fastmail_status
from providers.icloud import get_icloud_status
from providers.outlook import get_outlook_status
from providers.yahoo import get_yahoo_status


# Init
app = Flask(__name__)
dotenv.load_dotenv()

# Flask
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gmail")
def gmailStatus():
    return get_gmail_status()

@app.route("/outlook")
def outlookStatus():
    return get_outlook_status();

@app.route("/yahoo")
def yahooStatus():
    return get_yahoo_status();

@app.route("/icloud")
def icloudStatus():
    return get_icloud_status();

@app.route("/fastmail")
def fastmailStatus():
    return get_fastmail_status();
