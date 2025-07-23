from urllib.request import urlopen, Request
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from cachetools import TTLCache

cache = TTLCache(maxsize=10, ttl=300)
def get_fastmail_status():
    if "status" in cache:
        return cache["status"]
    with sync_playwright() as plw:
        browser = plw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://fastmailstatus.com/")
        page.wait_for_load_state("networkidle")
        html = page.content()
        browser.close()
    cache["status"] = html
    return html
