from bs4 import BeautifulSoup
from books_scraping.locators.book_locator import BookLocator
from books_scraping.parsers.book_parser import BookParser


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BookLocator.BOOKS
        books = self.soup.select(locator)
        return [BookParser(e) for e in books]
