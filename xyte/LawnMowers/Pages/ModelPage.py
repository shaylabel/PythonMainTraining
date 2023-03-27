from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from xyte.LawnMowers.Pages.locators import ModelPageLocators


class ModelPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_model(self):
        print('Try to click on add model')
        add_model = self.driver.find_element(*ModelPageLocators.ADD_MODEL)
        add_model.click()

    def fill_model(self,model_name):
        print('Try to fill model page')

    def delete_model(self,model_name):
         print('Try to delete model ')
