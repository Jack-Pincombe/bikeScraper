from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from selenium import webdriver
import re
import csv
import platform

list = []

def setUpSelenium():
    host = platform.system()
    if host == 'Linux':
        firefox_path = "/home/jack/Desktop/"
    else:
        firefox_path = "/Users/jackpincombe/Desktop"

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
    bikes = bsObj.findAll('h3')
    prices = bsObj.findAll('span', {'class': 'price-is'})
    for bike in range(10):
        bikeDetail = str(bikes[bike].get_text()).strip()
        price =str((getBikePrice(prices[bike].get_text()))).strip()

        bike = [bikeDetail, price]

        list.append(bike)

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

def addToCsv(list):
    with open('bikes.csv', 'w+') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        for i in list:
            csvWriter.writerow(i)

def readCSV():
    with open("bikes.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print("The cost of a" + row[0] + " is " + row[1])
    list = []

def __main__():
    setUpSelenium()
    siteMove()
    addToCsv(list)

readCSV()