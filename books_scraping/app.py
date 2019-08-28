import requests
import logging
from books_scraping.pages.books import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('books_scraping')


page_content = requests.get('http://books.toscrape.com/').content

page = BookPage(page_content)
books = page.books

for page in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page + 1}.html'
    page_content = requests.get(url).content
    logger.debug(f'Managed to get page_content from page nr `{page + 1}`')
    page = BookPage(page_content)
    books.extend(page.books)

for book in books:
    print(book)
