from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class WelcomePageLocators(object):
    pass


class LoginPageLocators(object):
    USER = (By.NAME, 'username')
    PW = (By.NAME, 'password')
    LOGIN = (By.CSS_SELECTOR,'button[class*="_acan"]')

class WelcomePageLocators(object):
    MODElS_SIDE_BAR = (By.LINK_TEXT, 'Profile')

class ModelPageLocators(object):
    ADD_MODEL = (By.CSS_SELECTOR, 'span[class*="mantine-1t9xh9a"]')
    MODEL_NAME = (By.ID,'mantine-fyukqfg4a')
    SAVE_MODEL = (By.CSS_SELECTOR,'button[class*="mantine-UnstyledButton-root"]')
    DELETE_MODEL = By.CSS_SELECTOR, 'span[class*="mantine-1t9xh9a mantine-Button-label"]'