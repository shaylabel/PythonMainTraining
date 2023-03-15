import unittest

import pytest

from PythonCharm.Python.Selenium.googleall.GogglePages.GoogleMain import GoogleMain
from PythonCharm.Python.Selenium.googleall.GoogleTests.BaseSelenium import BaseSelenium


def setUp(self):
    print('Test Start')


def tearDown(self):
    print('teat down')

@pytest.fixture
def fixture_before():
    # return [Fruit("apple"), Fruit("banana")]
    print ('\n into pixture')
    base=BaseSelenium()
    driver = base.selenium_init("https://www.google.com")
    return driver



@pytest.mark.parametrize(
   'pattern',
     [
            ('dog'),
            ('horse'),
        ]
    )

def test_google_multiple(pattern):
    print ('into test1',pattern)
    base=BaseSelenium()
    driver= base.selenium_init("https://www.google.com")
    main = GoogleMain(driver)
    main.searchForPattern(pattern)
    driver.close()

def test_google_cat(fixture_before):
    print ("\n into test2")
    driver= fixture_before
    main = GoogleMain(driver)
    main.searchForPattern("cat")
    driver.close()

def test_google_pixture_params(fixture_before):
    print ("\n into test2")
    driver= fixture_before
    main = GoogleMain(driver)
    main.searchForPattern('pattern')
    driver.close()


def test_google_pixture_params(fixture_before):
    print ("\n into test2")
    driver= fixture_before
    main = GoogleMain(driver)
    main.search_for_pattern_updated('cat')
    driver.close()

def test_google_pixture_params():
    print ("\n into test2")

