#!/jack/bin/env python

from selenium import webdriver

pageNo = 5

def siteNum(pageNo):
    buttonPath = """/html/body/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/ol/li["""+ str(pageNo) + """]/a"""
    return(buttonPath)
    #while i != 3:

firefox_path = "/home/jack/Desktop/"

driver = webdriver.Firefox(firefox_path)
driver.get('https://www.superbikefactory.co.uk/used-motorcycles-macclesfield-cheshire')

while pageNo != 3:
    driver.find_element_by_xpath(
        siteNum(pageNo)).click()

    pageNo -= 1

for i in range(10):
    driver.find_element_by_xpath(
        siteNum(pageNo)).click()
    print(driver.current_url)

print("Finished")





