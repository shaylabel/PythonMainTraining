import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Instgram.Pages.LoginPage import LoginPage
from Instgram.Pages.ProfilePage import ProfilePage
from Instgram.Pages.WelcomePage import WelcomePage
from Instgram.Tests.Base import Base


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(Base.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    login = LoginPage(driver)
    login.login(Base.user_name,Base.pw)

    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestGetInstegramDetails(Base):

    def test_get_account_details(self):
        welcome = WelcomePage(self.driver)
        profile = ProfilePage(self.driver)

        welcome.click_on_side_menu("Profile")
        account_details = profile.get_account_details()
        assert len(account_details) == 3 ,'one or more of account details is missing'

    def test_get_user_details(self):
        welcome = WelcomePage(self.driver)
        profile = ProfilePage(self.driver)

        welcome.click_on_side_menu("Profile")
        user_details = profile.get_user_details()
        assert len(user_details) == 6 ,'one or more of user details is missing'

