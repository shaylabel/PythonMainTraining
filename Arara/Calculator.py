from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from Arara.SeleniumBase import SeleniumBase


class Calculator(SeleniumBase):



    selenium_base = SeleniumBase()
    driver = selenium_base.selenium_start('https://www.calculator.net/')

    loan_link = driver.find_element(By.PARTIAL_LINK_TEXT,'Loan')
    loan_link.click()
    compound_drop_down = driver.find_element(By.ID,'ccompound')
    compound_select = Select(compound_drop_down)
    compound_select.select_by_value('monthly')
    compound_select.select_by_index('2')
    selenium_base.selenium_end(driver)