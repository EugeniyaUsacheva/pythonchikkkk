from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)
success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)
driver.quit()