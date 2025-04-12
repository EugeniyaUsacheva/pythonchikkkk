import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установить задержку в 45 секунд
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать кнопки 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ждать появления результата 15 (до 50 секунд)
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    assert result, "15"