import pytest
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    calc = SlowCalculatorPage(driver)
    calc.open()
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    assert calc.get_result(15), "Результат равен 15"
