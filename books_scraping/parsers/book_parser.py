import re
from bs4 import BeautifulSoup
from books_scraping.locators.book_details_locators import BookDetailsLocators


class BookParser:
    def __init__(self, parent: BeautifulSoup):
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.title} costs £{self.price}, stars: {self.rating}>'

    @property
    def title(self):
        locator = BookDetailsLocators.TITLE
        title = self.parent.select_one(locator)
        return title.attrs['title']

    @property
    def price(self):
        return 25.5  # just to see if everything else works

    @property
    def rating(self):
        locator = BookDetailsLocators.RATING
        tag = self.parent.select_one(locator)
        classes = tag.attrs['class']
        rating = [r for r in classes if r != 'star-rating']
        return rating[0]


""" Price throws an ERROR - NoneType doesn't have attribute group

        locator = BookDetailsLocators.PRICE
        price_with_symbol = self.parent.select_one(locator).string
        pattern = '£(\d\.\d)'
        matches = re.search(pattern, price_with_symbol)
        price = matches.group(1)
        return float(price)

"""