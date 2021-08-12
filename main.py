# Developer: Attiqa Sheikh
# File: main.py
# Purpose: Takes in a wikipedia link and prints out the title
# the hyperlinks, and most common words
 
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

#takes in the wikipedia link
response = requests.get(url="https://en.wikipedia.org/wiki/Artificial_intelligence")
soup = BeautifulSoup(response.content, 'html.parser')

#finds and prints the title on the wikipedia page
title = soup.find(id="firstHeading")
print("TITLE: " + title.string)

#finds and prints all of the hyperlinks within the wikipedia page
hyperlink = {}
for link in soup.find_all("a"):
    url = link.get("href", "")
    if "/wiki/" in url:
        hyperlink[link.text.strip()] = url
print(hyperlink)

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
#prints out the most common words starting from the most common to the least common
#each words has a number beside it demonstrating how many times each word occurs in the page
print(c.most_common())
