from bs4 import BeautifulSoup

NORMAL_HTML = '''<html lang = "en">
< head ></head >
< body >
<article class="product">
                <img class = "resize " src="images/copy/p3.jpg" title ="product1">
                <div class="info__container">
                    <h3>Mini Scented Mist</h3>
                    <span class="price">Rm 220</span>
                </div>
            </div>


</body ></html >'''

soup = BeautifulSoup(NORMAL_HTML, 'html.parser')

def find_title_name():
    locator = 'article.product img '
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)


def img_link():
    locator = 'article.product img.resize'
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['src']
    print(item_name)

img_link()





find_title_name()




