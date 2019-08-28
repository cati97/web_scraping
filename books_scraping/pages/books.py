import re
import logging
from bs4 import BeautifulSoup
from books_scraping.locators.book_locator import BookLocator
from books_scraping.parsers.book_parser import BookParser

logger = logging.getLogger('book_scraping.books')  # inherits basicConfig from parent


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookLocator.BOOKS
        books = self.soup.select(locator)
        logging.debug('Creating book objects.....')
        return [BookParser(e) for e in books]

    @property
    def page_count(self):
        content = self.soup.select_one(BookLocator.PAGER).string
        pattern = 'Page \d* of (\d*)'
        matches = re.search(pattern, content)
        return int(matches.group(1))
