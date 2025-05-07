from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self, expected_result):
        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, str(expected_result))
        )
