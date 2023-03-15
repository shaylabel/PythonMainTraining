from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Arara.SeleniumBase import SeleniumBase


class GetText(SeleniumBase):
    selenium_base = SeleniumBase()
    driver = selenium_base.selenium_start('https://demo.guru99.com/test/newtours/')

    user = driver.find_element(By.NAME, 'userName')
    pw = driver.find_element(By.NAME, 'password')
    login = driver.find_element(By.NAME, 'submit')

    user.click()
    user.send_keys("tutorial")
    user.send_keys(Keys.ENTER)

    pw.click()
    pw.send_keys("tutorial")
    pw.send_keys(Keys.ENTER)

    login.click()
    sleep(3)

    sleep (3)


    selenium_base.selenium_end(driver)