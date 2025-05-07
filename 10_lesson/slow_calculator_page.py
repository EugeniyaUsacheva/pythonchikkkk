import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы медленного калькулятора.

        :param driver: webdriver.Chrome - экземпляр веб-драйвера для управления браузером.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    @allure.step("Открытие страницы медленного калькулятора")
    def open(self):
        """
        Открывает страницу медленного калькулятора.

        :return: None
        """
        self.driver.get(self.url)

    @allure.step("Установка задержки в {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку в поле ввода.

        :param seconds: int - количество секунд задержки.
        :return: None
        """
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажатие на кнопку '{text}'")
    def click_button(self, text: str) -> None:
        """
        Нажимает на кнопку с указанным текстом.

        :param text: str - текст кнопки, на которую нужно нажать.
        :return: None
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    @allure.step("Получение результата вычисления")
    def get_result(self, expected_result: int) -> bool:
        """
        Ожидает появления результата вычисления на экране.

        :param expected_result: int - ожидаемый результат вычисления.
        :return: bool - True если ожидаемый результат появился на экране, иначе False.
        """
        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, str(expected_result))
        )

