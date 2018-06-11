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
    bikes = bsObj.findAll('h3')
    prices = bsObj.findAll('span', {'class': 'price-is'})
    for bike in range(10):

        print("The cost of " + str(bikes[bike].get_text()).lstrip(' ') + ' is ' + str((getBikePrice(prices[bike].get_text()))).lstrip())


def getBikeMake(tag):
    make = re.compile('\"View Vehicle Details\"(.*\S)/')

    if make.match(str(tag)):
        return make

def getBikePrice(tag):
    price = re.findall('(\S[1-9].*\d)', str(tag))[0]
    return price

getTitle('https://www.superbikefactory.co.uk/used-motorcycles-macclesfield-cheshire')