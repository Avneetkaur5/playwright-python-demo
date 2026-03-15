import time

import playwright
from playwright.sync_api import Page, expect


def test_google_launch(playwright):

    browser= playwright.chromium.launch(headless= False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")


def test_google_title(page:Page):
    page.goto("https://www.google.com/")
    # print(page.title())
    assert "Google" in page.title()



    time.sleep(5)