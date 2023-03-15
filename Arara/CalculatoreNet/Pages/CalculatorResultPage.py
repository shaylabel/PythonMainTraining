from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CalculatorResultPage(object):

    def __init__(self, driver):
        self.driver = driver
        print('into init')

    def generate_password(self):
        print('click on search button =')
        driver = self.driver
        button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "submit1")))

        button.click()

