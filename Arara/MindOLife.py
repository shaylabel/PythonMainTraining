from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from Arara.SeleniumBase import SeleniumBase


class MindOLife(SeleniumBase):



    selenium_base = SeleniumBase()
    driver = selenium_base.selenium_start('https://api.mindolife.com/')


    name = driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
    name.click()
    name.clear()
    name.send_keys("tsofen")
    name.send_keys(Keys.ENTER)

    pw = driver.find_element(By.CSS_SELECTOR, 'input[type=password]')

    pw.click()
    name.clear()
    pw.send_keys("tsofen@mindolife")
    pw.send_keys(Keys.ENTER)
    sleep(3)
    gataway = driver.find_element(By.PARTIAL_LINK_TEXT,'Gateway')
    act_text = gataway.text
    exp_text = "Gateways"
    assert act_text == exp_text, "Gataway did not found as expected"

    gataway.click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'a[data-toggle="dropdown"]').click()
    driver.find_element(By.CSS_SELECTOR,'a[data-target="#addGateway').click()
    selenium_base.selenium_end(driver)
