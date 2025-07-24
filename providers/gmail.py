from playwright.sync_api import sync_playwright
#from bs4 import BeautifulSoup
from cachetools import TTLCache

cache = TTLCache(maxsize=10, ttl=600)
def get_gmail_status():
    if "status" in cache:
        return cache["status"]
    with sync_playwright() as plw:
        browser = plw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com/appsstatus/dashboard/")
        page.wait_for_load_state("networkidle")
        html = page.content()
        browser.close()
    #soup = BeautifulSoup(html, "html.parser")
    cache["status"] = {
        "text":html
    }
    return {
        "text":html
    }
