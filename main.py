from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from selenium import webdriver
import re

url = "https://www.superbikefactory.co.uk/search_page.php?term=ducati-macclesfield-cheshire&ccto=9999&sort=h"
firefox_path = "/home/jack/Desktop/"

driver = webdriver.Firefox(firefox_path)
driver.get('https://www.superbikefactory.co.uk/used-motorcycles-macclesfield-cheshire')

def siteNum(pageNo):
    buttonPath = """/html/body/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/ol/li["""+ str(pageNo) + """]/a"""
    return(buttonPath)

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

        bikeDetail = str(bikes[bike].get_text()).strip()
        print("The cost of " + str(getBikeDetails(bikeDetail)) + ' is ' + str((getBikePrice(prices[bike].get_text()))).strip())


def getBikePrice(tag):
    price = re.findall('(\S[1-9].*\d)', str(tag))[0]
    return price

def getBikeDetails(tag):
    patern = re.compile('.+?(?=0%)')

    if patern.match(tag):
        return re.findall('.+?(?=0%)', tag)
    else:
        return tag

def siteMove():
    pageNo = 5
    while pageNo != 3:
        getTitle(driver.current_url)

        driver.find_element_by_xpath(
            siteNum(pageNo)).click()
        pageNo -= 1


    for i in range(10):
        driver.find_element_by_xpath(
            siteNum(pageNo)).click()
        getTitle(driver.current_url)

def __main__():
    siteMove()

__main__()