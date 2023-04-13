from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.guru99.com/test/newtours")
driver.maximize_window()

user = driver.find_element(By.NAME,"userName")
user.click()
user.clear()
user.send_keys("tutorial")

password = driver.find_element(By.NAME,"password")
password.click()
password.clear()
password.send_keys("tutorial")

submit_btn = driver.find_element(By.NAME,"submit")
submit_btn.click()

sleep(3)
driver.quit()