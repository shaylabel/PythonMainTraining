import unittest

from Arara.PageObjectExample.GooglePagesArara.GoogleResultsPage import GoogleResultsPage
from Arara.PageObjectExample.GooglePagesArara.GoogleSearchPage import GoogleSearchPage
from Arara.PageObjectExample.GoogleTestsArara.GoogleSeleniumBase import GoogleSeleniumBase


class SearchForAnimalTest(unittest.TestCase):



    def setUp(self):
        print('into set up \n')
        a=0


    def test_search_cat (self):

        google_selenium_base = GoogleSeleniumBase()
        driver = google_selenium_base.selenium_start('https://www.google.com/')
        google_results = GoogleResultsPage(driver)
        google_search = GoogleSearchPage(driver)

        google_results.demo_results('Into Demo Of Google Results')
        google_search.demo('Into Demo Of Google Search')
        google_search.search_for_text("cat")
        google_selenium_base.selenium_end(driver)

    def test_search_dog(self):
        google_selenium_base = GoogleSeleniumBase()
        driver = google_selenium_base.selenium_start('https://www.google.com/')
        google_results = GoogleResultsPage(driver)
        google_search = GoogleSearchPage(driver)
        google_results.demo_results('Into Demo Of Google Results')
        google_search.demo('Into Demo Of Google Search')
        google_search.search_for_text("dog")
        google_selenium_base.selenium_end(driver)

    def test_search_car(self):
        google_selenium_base = GoogleSeleniumBase()
        driver = google_selenium_base.selenium_start('https://www.google.com/')
        google_results = GoogleResultsPage(driver)
        google_search = GoogleSearchPage(driver)

        google_results.demo_results('Into Demo Of Google Results')
        google_search.demo('Into Demo Of Google Search')
        google_search.search_for_text("car")
        google_selenium_base.selenium_end(driver)





