from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class WelcomePageLocators(object):
    pass


class LoginPageLocators(object):
    USER = (By.ID, 'mantine-hlflckkm2')
    PW = (By.ID, 'mantine-zma8mduxv')
    LOGIN = (By.CSS_SELECTOR,'span[class*="mantine-14wyo4q"]')

class WelcomePageLocators(object):
    MODElS_SIDE_BAR = (By.HREF, '/models')

class ModelPageLocators(object):
    ADD_MODEL = (By.CSS_SELECTOR, 'span[class*="mantine-1t9xh9a"]')
    MODEL_NAME = (By.ID,'mantine-fyukqfg4a')
    SAVE_MODEL = (By.CSS_SELECTOR,'button[class*="mantine-UnstyledButton-root"]')