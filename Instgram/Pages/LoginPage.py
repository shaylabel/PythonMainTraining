from Instgram.Pages.InstgramLocators import LoginPageLocators

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

# login into system with allready created user and password
    def login(self,user_pattern,pw_pattern):
        print ('Try to login with user = '+ user_pattern+', pw = '+pw_pattern)
        user = self.driver.find_element(*LoginPageLocators.USER)
        pw = self.driver.find_element(*LoginPageLocators.PW)
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN)
        user.click()
        user.clear()
        user.send_keys(user_pattern)

        pw.click()
        pw.clear()
        pw.send_keys(pw_pattern)

        login_button.click()




