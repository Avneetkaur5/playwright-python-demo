from typing import Any, Generator

import pytest
from playwright.sync_api import Playwright, Page, sync_playwright

@pytest.fixture(scope='class')
def playwright_page(playwright: Playwright) -> Generator[Page, Any, None]:

    browser = playwright.chromium.launch(headless=False, slow_mo=0)
    context = browser.new_context()
    page = context.new_page()

    yield page

    #Teardown code - close the page and browser
    page.close()
    browser.close()



