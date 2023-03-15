from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Arara.SeleniumBase import SeleniumBase


class NewToursByGuro(SeleniumBase):

    selenium_base = SeleniumBase()
    driver = selenium_base.selenium_start("https://www.saucedemo.com/")


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

    price = driver.find_element(By.CLASS_NAME,'inventory_item_price')
    price_from_page= price.text
    print ('price from page =',price_from_page)
    price_from_page = price_from_page[1:5]
    print ('price from page after slice  =',price_from_page)
    assert price_from_page.endswith('.9') ,'the price of the first product is not 29.9 $ as expected'

    selenium_base.selenium_end(driver)