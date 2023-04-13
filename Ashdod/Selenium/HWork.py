from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.ebay.com/")
driver.maximize_window()

user = driver.find_element(By.ID,"gh-ac")
user.click()
user.clear()
user.send_keys("computer")

login_btn = driver.find_element(By.ID,"gh-btn")
login_btn.click()

sleep(3)
driver.quit()