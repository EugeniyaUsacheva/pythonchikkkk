from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()
green_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
)
green_box_text = green_box.text
print(green_box_text)
driver.quit()