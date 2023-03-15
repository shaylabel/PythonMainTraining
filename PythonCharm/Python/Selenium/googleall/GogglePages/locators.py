from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class ResultPageLocators(object):
    pass


class MainPageLocators(object):
    SEARCH = (By.NAME, 'q')

