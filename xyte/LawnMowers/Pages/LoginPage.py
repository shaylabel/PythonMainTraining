from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PythonCharm.Python.Selenium.googleall.GogglePages.locators import MainPageLocators
from xyte.LawnMowers.Pages.locators import LoginPageLocators


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

# login into system
    def login(self,user_pattern,pw_pattern):
        print ('Try to login with user = '+ user_pattern+', pw = '+pw_pattern)
        user = self.driver.find_element(*LoginPageLocators.USER)
        pw = self.driver.find_element(*LoginPageLocators.PW)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN)
        user.click()
        user.clear()
        user.send_keys(user_pattern)

        pw.click()
        pw.clear()
        pw.send_keys(pw_pattern)

        login_button.click()



    # def search_for_pattern_updated(self,pattern):
    #     try:
    #         search = self.driver.find_element(*MainPageLocators.SEARCH)
    #         search.click
    #         search.send_keys(pattern)
    #         search.send_keys(Keys.ENTER)
    #
    #     except:
    #         print ('exeption found')
    #
    #
    #     finally:
    #         print ('into finally')
