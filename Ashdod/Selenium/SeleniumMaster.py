
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class SeleniumMaster():

    def selenium_start(self,url):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        driver.maximize_window()
        return driver

    def selenium_close(self,driver):
        driver.quit()



