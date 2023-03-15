from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.googleall.GogglePages.locators import MainPageLocators


class GoogleMain(object):


    def __init__(self, driver):
        self.driver = driver
        print ('into init')

    def demo(self):
        print ('into demo at google main')

    def searchForPattern(self,pattern):
        print ('into search for pattern')
        try:
            search = self.driver.find_element(*MainPageLocators.SEARCH)
            search.click()
            search.clear()
            search.send_keys(pattern)
            search.send_keys(Keys.ENTER)
        except:
            print ('exeption found')

        finally:
            print ('into finally')

    def search_for_pattern_updated(self,pattern):
        try:
            search = self.driver.find_element(*MainPageLocators.SEARCH)
            search.click
            search.send_keys(pattern)
            search.send_keys(Keys.ENTER)

        except:
            print ('exeption found')


        finally:
            print ('into finally')
