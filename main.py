import requests 
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"

#Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

#Setp 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

#Steo 3: HTML Tree Traversal

#comment
markup = "<p><!--this is a comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

#Get the title of the HTML page
title = soup.title

#Get all the paragraphs from HTML page
paras = soup.find_all('p')
print(paras)

#Get all the anchor tags from HTML page
anchors = soup.find_all('a')
print(anchors)

#Get the first element in the HTML page
print(soup.find('p'))

#Get the classes of any element in the HTML page
print(soup.find('p')['class'])

#Find all the elements with class lead
print(soup.find_all(class_='lead'))

#Get the text from the tags/soups
print(soup.get_text())

#Get all the anchor tags from HTML page
anchors = soup.find_all('a')
all_links =set()
# Get all the link on  the page
for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://books.toscrape.com/" +link.get('href')
        all_links.add(link)
        print(linkText)

default = soup.find(id='default')
print(default)

for item in default.strings:
    print (item)

print(default.parent)

print(default.parents)

for item in default.parents:
    print(item.name)

print(default.next_sibling.next_sibling)
print(default.previous_sibling.previous_sibling)

elem = soup.select('.messages')
print(elem)