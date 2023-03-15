import unittest

from ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain
from ImageAnalyze.ImageGoogleTests.BaseSelenium import BaseSelenium
from ImageAnalyze.Utils.ImagesUtils import ImagesUtils


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













