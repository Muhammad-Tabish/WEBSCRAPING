

from bs4 import BeautifulSoup

NORMAL_HTML = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <article class="product">
        <img class = "resize " src="images/copy/p3.jpg" title ="product1">
        <article class="tab">
        <h3> <p Mini Scented Mist></p>
        </h3>
    
        <p class="price"  price1 ="Rm 22.20"></p>
        <p class="star rating Three">
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
        </p>
        </article>
    
    </article>

    

</body>
</html>'''

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

def find_price():
    locator = 'article.product p.price'
    item_price = soup.select_one(locator)
    item_name = item_price.attrs['price1']
    print(item_name)

def find_rating ():
    locator = 'article.product p.star rating'
    rating = soup.select_one(locator)
    classes = rating.attrs['class']
    rating_classes = [r for r in classes if r != 'star rating']
    print(rating_classes[0])

#find_rating()







find_price()
img_link()
find_title_name()




