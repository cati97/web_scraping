import re

from bs4 import BeautifulSoup

ITEM_HTML = '''
<html>
<head></head>
<body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                <i class="icon-ok"></i>
        In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>
    </article>
</li>
</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_book_title():
    locator = 'article.product_pod h3 a'
    link = soup.select_one(locator)
    link_title_attr = link.attrs['title']
    print(link_title_attr)


def find_price():
    locator = 'article.product_pod div.product_price p.price_color'
    price_with_symbol = soup.select_one(locator).string
    expression = '£(\d*\.\d*)'
    price = re.search(expression, price_with_symbol)
    print(float(price.group(1)))


def find_rating():
    locator = 'article.product_pod p.star-rating'
    price_tag = soup.select_one(locator)
    classes = price_tag.attrs['class']
    rating = "".join([name for name in classes if name != 'star-rating'])
    print(rating)


# find_book_title()
# find_price()
find_rating()
