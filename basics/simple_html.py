from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <p class='subtitle'>Paragraph with class </p>
        <p>New paragraph at that list! </p>
        <ul>
            <li>coffee</li>
            <li>tea</li>
            <li>water</li>
        </ul>
    </body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('p').string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    items_as_strings = [item.string for item in list_items]
    print(list_items)
    print(items_as_strings)


def find_tag_with_attribute():
    item = simple_soup.find('p', {'class': 'subtitle'})
    print(item.string)


def find_tag_without_attribute():
    paragraphs = simple_soup.find_all('p')
    without = [p for p in paragraphs if p not in p.attrs.get('class', [])]
    print(without)


find_list_items()
find_tag_with_attribute()
find_tag_without_attribute()
