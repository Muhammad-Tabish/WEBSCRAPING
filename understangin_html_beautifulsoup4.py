from bs4 import BeautifulSoup


SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This a title</h1>
<p class = "subtitle"> Hi</p>
<p> Here</p>
<ul>
   <li>hem</li>
   <li>eee</li>
   <li>ham</li>
   <li>fam</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_lists():
    lists = simple_soup.findAll('li')
    lists_content = [a.string for a in lists]
    print(lists_content)



def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)



def find_other_paragraphs():
    paragraphs = simple_soup.findAll('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)

find_title()
find_lists()
find_subtitle()
find_other_paragraphs()


