import pytest
import allure
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    """
    Фикстура для создания экземпляра веб-драйвера Chrome.

    :return: webdriver.Chrome - экземпляр веб-драйвера Chrome.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.feature("Тестирование медленного калькулятора")
@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы медленного калькулятора с задержкой 45 секунд.")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver: webdriver.Chrome) -> None:
    """
    Тест для проверки работы медленного калькулятора.

    :param driver: webdriver.Chrome - экземпляр веб-драйвера Chrome.
    :return: None
    """

    calc = SlowCalculatorPage(driver)

    calc.open()

    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    assert calc.get_result(15), "Результат равен 15"
