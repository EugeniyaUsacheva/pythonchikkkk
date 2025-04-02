from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("Sky")
sleep(2)
input_field.clear()
input_field.send_keys("Pro")
driver.quit()