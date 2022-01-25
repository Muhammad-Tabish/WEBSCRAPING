from bs4 import BeautifulSoup
normal_html = '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
       <h3>Tabish</h3>
       <p class="price" price="22.2"></p>
       <p class="star rating  Three">
         <i class="icon-star"></i>
         <i class="icon-star"></i>
         <i class="icon-star"></i>
       </p>
    
    
</body>
</html>
'''

soup = BeautifulSoup(normal_html, 'html.parser')
def find_rating ():
    locator = 'p.star rating'
    rating = soup.select_one(locator)
    classes = rating.attrs['class']
    rating_classes = [r for r in classes if r != 'star rating']
    print(rating_classes[0])

find_rating()