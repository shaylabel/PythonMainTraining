from xyte.LawnMowers.Pages.locators import WelcomePageLocators


class WelcomePage(object):


    def __init__(self, driver):
        self.driver = driver


# method for clicking over any link into side menu
    def click_on_side_menu(self,side_menu):
        models = self.driver.find_element(*WelcomePageLocators.MODElS_SIDE_BAR)
        models.click()


