from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
element = WebDriverWait(driver, 40)
pictures = element.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#award')))
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")
print(src)
driver.quit()