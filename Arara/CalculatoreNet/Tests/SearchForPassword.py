
from Arara.CalculatoreNet.Pages.CalculatorSearchPage import CalculatorSearchPage
from Arara.CalculatoreNet.Pages.CalculatorResultPage import CalculatorResultPage
from Arara.CalculatoreNet.Tests.Passwordbase import PasswordBase


class SearchForPassword(PasswordBase):
    calculator_base = PasswordBase()
    driver = calculator_base.selenium_start('https://www.calculator.net/')
    Calcolatur_search = CalculatorSearchPage(driver)
    Calcolatur_result = CalculatorResultPage(driver)

    Calcolatur_search.search_for_text('Password Generator')
    Calcolatur_search.click_on_link('Password')
    Calcolatur_result.generate_password()

    calculator_base.selenium_end(driver)
