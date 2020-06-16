import requests
from bs4 import BeautifulSoup
import os


class WebScrapper():
   wiki = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
   soup = BeautifulSoup(wiki.content, "html.parser")

    # function to get the title of the page
   def getTitle(self):
     title = self.soup.title.string
     return title

   # function to get all the links available
   def getWikiLinks(self):
       list = []
       for link in self.soup.find_all('a'):
           list.append(link.get('href'))
       return list

webs = WebScrapper()
print(webs.getTitle())
for x in webs.getWikiLinks():
    print (x, file=open("output.txt", "a")) # Saving links in TXT file