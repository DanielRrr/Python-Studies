from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
url = str(input())
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title)
