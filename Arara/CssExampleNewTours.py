from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Arara.SeleniumBase import SeleniumBase


class CssExample(SeleniumBase):
    selenium_base = SeleniumBase()
    driver = selenium_base.selenium_start('https://demo.guru99.com/test/newtours/reservation.php')
    names = driver.find_elements(By.NAME,'tripType')
    counter = 0
    one_way = driver.find_element(By.CSS_SELECTOR,'input[value=oneway]')
    one_way_text= one_way.text
    counter = counter+1

    assert counter == 1,'counter value is not 1 as expected'
    assert one_way_text.endswith('ne Way'), 'One way text is not as expected '

    one_way.click()

    print('One way button success to clicked')

    selenium_base.selenium_end(driver)