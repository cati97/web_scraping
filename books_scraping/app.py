import requests
from books_scraping.pages.books import BookPage

page_content = requests.get('http://books.toscrape.com/').content

page = BookPage(page_content)
books = page.books

for page in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page+1}.html'
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)

for book in books:
    print(book)
