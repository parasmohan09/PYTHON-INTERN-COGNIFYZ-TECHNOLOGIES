#web scrapper by using beautiful soup library in the python.
#TO DONE WEBSCRAPPING IN THE PYTHON WE CAN USE THE LIBRARY MODULE LIKE BEAUTIFUL SOUP AND WE CAN FOLLOWS SOME STEPS TO DONE SCRAPING IN THE PYTHON.

# THERE ARE TWO METHODS TO DONE WEB SCRAPPING
# 1.USING API.
# 2.USING BEAITIFULSOUP OR SCRAPY LIBRARY.

# WE CAN INSTALL SOME MODULE TO DONE THIS LIKE REQUEST MODULE,HTML5IB MODULE,AND BS4 MODULE IN THE BS4 BEAUTIFULSOUP IS PRESENT.

import requests
from bs4 import BeautifulSoup
url="https://cognifyz.com/"

#step 1. get the html.

r=requests.get(url)
html_content=r.content
# print(html_content)

# step 2 > parse the html webpage.

soup= BeautifulSoup(html_content,"html.parser")
# print(soup.prettify)

# step 3 > html traverse.

# in the html traverse we can check elements of web page in the python programm.

# commonly objects which is used in bs4
#1 tag-tittle,p,<a>,div,etc 
#2 beautifulsoup
#3 navigablestring print(type(tittle.string))
#4 comments.

# tag

# print(soup.title)
# it can be used in the web scarping when we scrap or traverse any webpage in the programm.

# print(soup.title.name)

# print(type(soup.title.string))

# print(soup.p)
# print(soup.p['class'])
# s=soup.a['class']
# print(s)
# m=soup.find_all('a')
# print(m)
# print(soup.find())

# print(soup.find('p').get_text())
# print(soup.get_text())

# now we can extract the urls present in the anchor tags.

# print(soup.a)
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
#     if(link.get('href') !='#'):
#      print(link.get('href'))
     
# head_tag=soup.head
# print(head_tag)
# print(head_tag.contents)
# title_tag=head_tag.contents[7]
# print(title_tag)

# .content and .children in the BeautifulSoup.

# .content: a tag children avialable as  list is also known as the .content in the python.
#.children : a tag children are available as generator in beutifulsoup is also known as the .children in the bs4.
# head_tag=soup.head
# # title_tag=head_tag.descendants
# print(head_tag.contents)

# comments special object in the BeautifulSoup library in the python..

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

# paras="<title>paras is the titile</title>"
# soup3=BeautifulSoup(paras)
# print(type(paras))

# now we can say that i am knowing all the basics how beautiful soup can be used, how it works,how we can done this,knowing steps of web scraping in the python.traverse html document in the python,how we can create the soup in the python,url, which library we can used and how ae can use it we know the all concept...





    
     
     

    







 





 











 
