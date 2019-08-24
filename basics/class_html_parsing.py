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


class ParseItemLocators:
    TITLE_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParseItem:
    """
    A class takes a page(part of it) and find properties of it
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def title(self):
        locator = ParseItemLocators.TITLE_LOCATOR
        link = self.soup.select_one(locator)
        link_title_attr = link.attrs['title']
        return link_title_attr

    @property
    def price(self):
        locator = ParseItemLocators.PRICE_LOCATOR
        price_with_symbol = self.soup.select_one(locator).string
        expression = '£(\d*\.\d*)'
        price = re.search(expression, price_with_symbol)
        return float(price.group(1))

    @property
    def rating(self):
        locator = ParseItemLocators.RATING_LOCATOR
        price_tag = self.soup.select_one(locator)
        classes = price_tag.attrs['class']
        rating = "".join([name for name in classes if name != 'star-rating'])
        return rating


item = ParseItem(ITEM_HTML)
print(item.rating)

print(ParseItem.__doc__)