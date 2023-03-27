


class WelcomePage(object):

    def __init__(self, driver):
        self.driver = driver


    def click_on_side_menu(self,side_menu):
        models = self.driver.find_element(side_menu)
        models.click()


