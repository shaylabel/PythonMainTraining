import unittest


class SearchForAnimal(unittest.TestCase):


    def setUp(self):
        print('into set up \n')
        a=0


    def test_1 (self):
        print('into test 1')
        assert 1 == 1 ,'1 in not 1 as exepcted '

    def test_2(self):
        print('into test 2')
        assert 1 == 2 , '1 is not 2 as exepcted '

    def test_3(self):
         print('into test 3')
         assert 2 == 2, '2 is not 2 as exepcted '

    def test_4(self):
         print('into test 4')
         assert 4 == 4, '4 is not 4 as exepcted '


    # def test_search_cat (self):
    #     google_selenium_base = GoogleSeleniumBase()
    #     driver = google_selenium_base.selenium_start('https://www.google.com/')
    #     google_results = GoogleResultsPage(driver)
    #     google_search = GoogleSearchPage(driver)
    #
    #     google_results.demo_results('Into Demo Of Google Results')
    #     google_search.demo('Into Demo Of Google Search')
    #     google_search.search_for_text("cat")
    #     google_selenium_base.selenium_end(driver)
    #
