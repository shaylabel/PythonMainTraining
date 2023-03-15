from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CalculatorSearchPage(object):

    def __init__(self, driver):
        self.driver = driver
        print('into init')


    # print the content for text
    def demo(self, text):
        print(text)


    def search_for_text(self, text):
        print ('try to find text =', text)
        driver = self.driver
        search = driver.find_element(By.NAME, "calcSearchTerm")
        search.click()
        search.clear()
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

    def click_on_link(self, text):
        print('try to click on link ', text)
        driver = self.driver
        link = driver.find_element(By.PARTIAL_LINK_TEXT,text)
        link.click()



