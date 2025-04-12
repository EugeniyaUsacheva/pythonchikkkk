import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_process(browser):
    wait = WebDriverWait(browser, 10)

    # Открываем сайт
    browser.get("https://www.saucedemo.com/")

    # Логин
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()

    # Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "checkout"))).click()

    # Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Женя")
    browser.find_element(By.ID, "last-name").send_keys("Усачева")
    browser.find_element(By.ID, "postal-code").send_keys("847474774")
    browser.find_element(By.ID, "continue").click()

    # Проверяем Total
    total_label = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_label.text

    # Проверка итоговой суммы
    assert total_text == "Total: $58.29"
