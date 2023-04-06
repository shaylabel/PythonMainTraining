from telnetlib import EC

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Instgram.Pages.InstgramLocators import ProfilePageLocators


class ProfilePage(object):

    def __init__(self, driver):
        self.driver = driver

# get all account details and return  it as  dictionary (posts, followed ...)
    def get_account_details(self):
        elements = self.driver.find_elements(*ProfilePageLocators.ACOUNT_DETAILS)
        account_details = {}

        for element in elements:
            pattern = element.text
            indx = pattern.index(" ")
            val = pattern[:indx]
            key = pattern[indx:]
            account_details[key] = val

        return account_details

    # get all user details and return  it as  dictionary (user, name, email ...)
    def get_user_details(self):
        edit = self.driver.find_elements(*ProfilePageLocators.EDIT_BTN)
        edit.click()
        user_details = {}

        name_text = self.driver.find_element(*ProfilePageLocators.NAME_FROM_EDIT).text
        user_details['name'] = name_text

        user_text = self.driver.find_element(*ProfilePageLocators.USER_FROM_EDIT).text
        user_details['user'] = user_text

        bio_text = self.driver.find_element(*ProfilePageLocators.BIO_FROM_EDIT).text
        user_details['bio'] = bio_text

        email_text = self.driver.find_element(*ProfilePageLocators.EMAIL_FROM_EDIT).text
        user_details['email'] = email_text

        phone_text = self.driver.find_element(*ProfilePageLocators.PHONE_FROM_EDIT).text
        user_details['phone'] = phone_text

        gender_text = self.driver.find_element(*ProfilePageLocators.GENDER_FROM_EDIT).text
        user_details['gender'] = gender_text

        return user_details
