#!/jack/bin/env python

from selenium import webdriver
firefox_path = "/home/jack/Desktop/"

driver = webdriver.Firefox(firefox_path)
driver.get('https://www.superbikefactory.co.uk/used-motorcycles-macclesfield-cheshire')

driver.find_element_by_xpath(
    """/html/body/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/ol/li[5]/a""").click()

driver.find_element_by_xpath(
    """/html/body/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/div[3]/ol/li[4]/a""").click()

for i in range(10):
    driver.find_element_by_xpath(
        """/html/body/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[3]/ol/li[3]/a""").click()
    print(driver.current_url)

print("Finished")

def autoClickNext():
    pass
