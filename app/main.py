from urllib.request import urlopen
from bs4 import BeautifulSoup
import dotenv
import os
import uuid

dotenv.load_dotenv()


def main():
    print("Hello flask!")
