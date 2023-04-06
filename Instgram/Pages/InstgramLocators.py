from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USER = (By.NAME, 'username')
    PW = (By.NAME, 'password')
    LOGIN = (By.CSS_SELECTOR, 'button[class*="_acan _acap"]')


class WelcomePageLocators(object):
    pass

class ProfilePageLocators(object):
    ACOUNT_DETAILS = (By.CSS_SELECTOR, 'li.xl565be.x2pgyrj.x1m39q7l.x1uw6ca5')
    EDIT_BTN = (By.LINK_TEXT, 'Edit profile')
    NAME_FROM_EDIT = (By.ID, "pepName")
    USER_FROM_EDIT = (By.ID, "pepUsername")
    BIO_FROM_EDIT = (By.ID, 'pepBio')
    EMAIL_FROM_EDIT = (By.ID, 'pepEmail')
    PHONE_FROM_EDIT = (By.ID, 'pepPhoneNumber')
    GENDER_FROM_EDIT = (By.ID, 'pepGender')
