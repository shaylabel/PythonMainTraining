from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class WelcomePageLocators(object):
    pass


class LoginPageLocators(object):
    USER = (By.ID, 'mantine-hlflckkm2')
    PW = (By.ID, 'mantine-zma8mduxv')
    LOGIN = (By.CSS_SELECTOR,'span[class*=mantine-14wyo4q]')

class WelcomePageLocators(object):
    MODElS_SIDE_BAR = (By.HREF, '/models')