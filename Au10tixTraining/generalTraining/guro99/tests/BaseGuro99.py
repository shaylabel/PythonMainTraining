from selenium import webdriver


class BaseGuro99(object):


    def __init__(self):
        driver = webdriver.Chrome(executable_path="C:\Selenium\Drivers\‏‏Chrome104\chromedriver.exe")
        self.driver = driver




    def selenium_start(self,url):

        driver=self.driver
        driver.get(url)
        driver.maximize_window()
        return driver



