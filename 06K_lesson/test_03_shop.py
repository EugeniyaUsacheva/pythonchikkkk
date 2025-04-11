import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # Запуск веб-драйвера (например, Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_process(browser):
    # Открываем сайт
    browser.get("https://www.saucedemo.com/")

    # Заполняем поля для логина
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    browser.find_element(By.ID, "shopping-cart-link").click()

    # Нажимаем на кнопку Checkout
    browser.find_element(By.ID, "checkout").click()

    # Заполняем форму для чекаута
    browser.find_element(By.ID, "first-name").send_keys("Женя")
    browser.find_element(By.ID, "last-name").send_keys("Усачева")
    browser.find_element(By.ID, "postal-code").send_keys("847474774")
    browser.find_element(By.ID, "continue").click()

    # Проверяем, что на странице есть элемент с итоговой суммой
    total_label = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_label.text

    # Проверка итоговой суммы
    assert total_text == "Total: $58.29"