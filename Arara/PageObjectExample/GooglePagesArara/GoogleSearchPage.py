from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GoogleSearchPage(object):

    def __init__(self, driver):
        self.driver = driver
        print('into init')


    # print the content for text
    def demo(self, text):
        print(text)


    def search_for_text(self,text):
        print ('try to find text =',text)
        driver = self.driver
        search = driver.find_element(By.NAME, "q")
        search.click()
        search.clear()
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

