from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class GoogleSeleniumBase():

    def __init__(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    def selenium_start(self,url):
        print ('test start')
        driver=self.driver
        driver.get(url)
        driver.maximize_window()
        return driver

    def selenium_end (self , driver):
        print ('test end')
        driver.quit()
