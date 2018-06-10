from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
import re

url = "https://www.superbikefactory.co.uk/search_page.php?term=ducati-macclesfield-cheshire&ccto=9999&sort=h"

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    if html is None:
        print("Shit has hit the fan")
    else:
        bsObj = bs(html.read(), "html.parser")
        getAllPrices(bsObj)

def getAllPrices(bsObj):
    list = []

    for tag in bsObj.findAll('span', {'class': 'price-is'}):
        list.append(getBikePrice(tag))

    print(len(list))

def getBikePrice(tag):
    price = re.findall('(\S[1-9].*\d)', str(tag))[0]
    print("The price of the bike is " + price)

getTitle(url)


