import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Фикстура для запуска и завершения драйвера
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

# Функция для получения цвета фона элемента
def get_background_color(driver, field_name):
    element = driver.find_element(By.ID, field_name)
    return element.value_of_css_property("background-color")

# Тест на заполнение формы
def test_fill_form(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # Заполнение всех полей кроме zip
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Отправка формы
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # zip должно быть красным
    zip_code_color = get_background_color(driver, "zip-code")
    assert "rgba(248, 215, 218, 1)" in zip_code_color, "Zip code не подсвечен красным"

    # Остальные поля должны быть зелеными
    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in green_fields:
        color = get_background_color(driver, field)
        assert "rgba(209, 231, 221, 1)" in color, f"Поле {field} не подсвечено зелёным"