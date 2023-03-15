import unittest

from ImageAnalyze.ImageGogglePages.GoogleMain import GoogleMain
from ImageAnalyze.ImageGoogleTests.BaseSelenium import BaseSelenium
from ImageAnalyze.Utils.ImagesUtils import ImagesUtils



class SeleniumPytest(unittest.TestCase,BaseSelenium):

    def setUp(self):
        print ('Test Start')
        base = BaseSelenium()
        driver = base.selenium_init("https://www.google.com")
        images_utils = ImagesUtils(driver)
        self.images_utils = images_utils
        self.base = base


    def test_image_compare(self):

        path_ref_image = "..//Images//Error.png"

        # box parameters :x, y, x+width, y+hight
        box = (650, 140, 980, 270)
        self.images_utils.compare_image_rectangle(path_ref_image, box, 'name1')

        self.base.selenium_end()











