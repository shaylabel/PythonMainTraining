from selenium.webdriver.common.by import By

class WelcomePage(object):

    def __init__(self, driver):
        self.driver = driver

    # generic method for clicking over any link into left side menu
    def click_on_side_menu(self, side_menu_pattern):
        side_menu = self.driver.find_element(By.LINK_TEXT, side_menu_pattern)
        side_menu.click()
