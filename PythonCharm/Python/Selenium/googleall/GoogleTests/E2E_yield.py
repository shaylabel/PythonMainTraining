import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.close()



@pytest.mark.usefixtures("setup")   # define here at class level,can be define at test level as well
class TestExampleOne:
    def test_title(self):
        print('into test 1')
    def test_google(self):
        print("Verify content on the page")
        self.driver.find_element(By.NAME, "q").send_keys("hhhhh")

    @pytest.mark.usefixtures("setup1")
    def test_google(self):
        print("Verify content on the page")
        self.driver.find_element(By.NAME, "q").send_keys("hhhhh")