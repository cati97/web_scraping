import re
from bs4 import BeautifulSoup
from books_scraping.locators.book_details_locators import BookDetailsLocators


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent: BeautifulSoup):
        self.parent = parent

    def __repr__(self):
        return f'<Title: {self.title} costs £{self.price}, stars: {self.rating}>'

    @property
    def title(self):
        locator = BookDetailsLocators.TITLE
        title_tag = self.parent.select_one(locator)
        title = title_tag.attrs['title']
        return title

    @property
    def price(self):
        locator = BookDetailsLocators.PRICE
        price_with_symbol = self.parent.select_one(locator).string
        pattern = '£(\d*\.\d*)'
        matches = re.search(pattern, price_with_symbol)
        price = matches.group(1)
        return float(price)

    @property
    def rating(self):
        locator = BookDetailsLocators.RATING
        tag = self.parent.select_one(locator)
        classes = tag.attrs['class']
        rating = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating[0])
        return rating_number
