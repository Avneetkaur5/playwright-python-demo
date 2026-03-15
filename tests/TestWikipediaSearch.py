
import pages.wikiSearch

def test_search_lands_on_wikipedia(self, page):
    """The Main Page title contains 'Wikipedia'."""

    page.goto()