from urllib.request import urlopen, Request
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from cachetools import TTLCache

cache = TTLCache(maxsize=10, ttl=600)
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
    soup = BeautifulSoup(html, "html.parser")
    success = soup.find("h2", class_="main-status__heading")
    cache["status"] = {
        "text":success
    }
    return {
        "text":success
    }
