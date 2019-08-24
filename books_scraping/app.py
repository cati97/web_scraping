import requests

from books_scraping.pages.books import BookPage

page_content = requests.get('http://books.toscrape.com/').content

page = BookPage(page_content)

for b in page.books:
    print(b)
