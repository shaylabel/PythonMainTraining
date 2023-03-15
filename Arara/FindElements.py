from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Arara.SeleniumBase import SeleniumBase


class FindElements (SeleniumBase):

    print ('Test start')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    user = driver.find_element(By.ID,'user-name')
    pw = driver.find_element(By.ID,'password')
    login = driver.find_element(By.ID,'login-button')

    user.click()
    user.send_keys("standard_user")
    user.send_keys(Keys.ENTER)
    pw.click()
    pw.send_keys("secret_sauce")
    pw.send_keys(Keys.ENTER)
    login.click()
    sleep (3)

    prices = driver.find_elements(By.CLASS_NAME,'inventory_item_price')
    length= len(prices)

    price_1 = prices[1]
    price_2 = prices[2]
    price_1_text = price_1.text

    length_price1 = len(price_1_text)
    print ('the price of price1 is ',price_1.text)
    print('the proce of price_2 is ', price_2.text)

    driver.quit()
    print ('Test close')