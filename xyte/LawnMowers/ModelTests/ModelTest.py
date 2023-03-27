import pytest
import self
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from xyte.LawnMowers.Pages.LoginPage import LoginPage
from xyte.LawnMowers.Pages.ModelPage import ModelPage
from xyte.LawnMowers.Pages.WelcomePage import WelcomePage


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://partners.xyte.io/auth/sign-in")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestAddModel:
    def test_create_model(self):
        login = LoginPage(self.driver)
        welcome = WelcomePage(self.driver)
        model = ModelPage(self.driver)
        name_to_create = 'test1'

        login.login("kobyd100@gmail.com","zxcvASDF12!@")
        welcome.click_on_side_menu(*WelcomePage.MODElS_SIDE_BAR)
        model.fill_model(name_to_create)
        model.delete_model(name_to_create)        # needed in order to permit add other models at comming test

    def test_delete_model(self):
        login = LoginPage(self.driver)
        welcome = WelcomePage(self.driver)
        model = ModelPage(self.driver)
        name_to_delete = 'test_to_delete'

        login.login("kobyd100@gmail.com","zxcvASDF12!@")
        welcome.click_on_side_menu(*WelcomePage.MODElS_SIDE_BAR)
        model.fill_model(name_to_delete)
        model.delete_model(name_to_delete)