import pytest
from selenium import webdriver
from saucedemo_page import SauceDemoPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_process(browser):
    page = SauceDemoPage(browser)

    page.open()
    page.login("standard_user", "secret_sauce")
    page.add_items_to_cart()
    page.go_to_cart()
    page.checkout("Женя", "Усачева", "847474774")

    total = page.get_total_text()
    assert total == "Total: $58.29"
