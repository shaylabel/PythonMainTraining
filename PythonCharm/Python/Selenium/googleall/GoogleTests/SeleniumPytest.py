import unittest


from PythonCharm.Python.Selenium.googleall.GogglePages.GoogleMain import GoogleMain
from PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


class SeleniumPytest(unittest.TestCase,BaseSelenium):



    def setUp(self):
        print ('Test Start')



    def test_google_cat(self):
        base=BaseSelenium()
        driver= base.selenium_init("https://www.google.com")
        main=GoogleMain(driver)
        main.searchForPattern("cat")

    def test_google_dog(self):
        base=BaseSelenium()
        driver= base.selenium_init("https://www.google.com")
        main=GoogleMain(driver)
        main.searchForPattern("Dog")









