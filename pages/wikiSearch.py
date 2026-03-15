import re

from playwright.sync_api import Page, expect
from pages.base import playwright_page

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"

def search_and_open_first_result(page, query: str) -> str:
    """
    Navigate to Wikipedia, type *query* in the search box, submit,
    click the first proper article result, and return the page title text.
    """

    # 1. Land on the Main Page
    page.goto(WIKIPEDIA_URL)
    expect(page).to_have_title("Wikipedia")

    # 2. Type the search query
    search_input=page.get_by_role("combobox", name=("search"))
    search_input.fill(query)

    # 3. Submit (press Enter – avoids depending on a specific button label)
    search_input.press("Enter")

    # 4. Wait for results / article page to settle
    page.wait_for_load_state("domcontentloaded")

    # Wikipedia has two paths after a search:
    #   a) Exact-match  → redirected straight to the article
    #   b) Search-results page → list of hits; click the first title link
    if "/wiki/Special:Search" in page:
        first_result = page.locator("ul.mw-search-results li.mw-search-result a").first
        first_result.click()
        page.wait_for_load_state("domcontentloaded")

    # 5. Return the article heading so tests can assert on it
    return page.locator("#firstHeading").inner_text()