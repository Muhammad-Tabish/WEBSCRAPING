

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
class ParsedItemLocators:
    Name_locator = 'article.product img '
    img_link = 'article.product img.resize'
    price_locator = 'article.product p.price'
class ParsedItem:
   def __init__(self, page):
       self.soup = BeautifulSoup(page, 'html.parser')
   @property
   def name(self):
     locator = ParsedItemLocators.Name_locator
     item_link = self.soup.select_one(locator)
     item_name = item_link.attrs['title']
     return item_name

   @property
   def img_link(self):
     locator = ParsedItemLocators.img_link
     item_link = self.soup.select_one(locator)
     item_name = item_link.attrs['src']
     return  item_name
   @property
   def price(self):
     locator = ParsedItemLocators.price_locator
     item_price = self.soup.select_one(locator)
     item_name = item_price.attrs['price1']
     return  item_name

  def rating ():
    locator = 'article.product p.star rating'
    rating = soup.select_one(locator)
    classes = rating.attrs['class']
    rating_classes = [r for r in classes if r != 'star rating']
    print(rating_classes[0])

item = ParsedItem(NORMAL_HTML)
print(item.name)









