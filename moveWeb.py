import re
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs


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
    for container in bsObj.findAll('div', {'class': 'container'}):
        price = getBikePrice(container.findAll('span', {'class': 'price-is'}))
        text = getBikeMake(container.find('h3'))


        print("The cost of " + str(getBikeMake(text)) + " is " + str(getBikePrice(price)))

def getBikeMake(tag):
    make = re.compile('\"View Vehicle Details\"(.*\S)/')

    if make.match(str(tag)):
        return make

def getBikePrice(tag):
    price = re.compile('(\S[1-9].*\d)')

    if price.match(str(tag)):
        return price

getTitle('https://www.superbikefactory.co.uk/used-motorcycles-macclesfield-cheshire')