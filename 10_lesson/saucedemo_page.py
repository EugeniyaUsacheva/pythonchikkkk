import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemoPage:
    """
    Класс для взаимодействия со страницей SauceDemo.

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера Selenium.
        wait (WebDriverWait): Объект ожидания для управления временем ожидания элементов.
    """

    def __init__(self, driver):
        """
        Инициализация класса SauceDemoPage.

        Параметры:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие главной страницы SauceDemo")
    def open(self) -> None:
        """Открывает главную страницу SauceDemo."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Вход на сайт с учетными данными: {username}")
    def login(self, username: str, password: str) -> None:
        """Выполняет вход на сайт с указанными учетными данными."""
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self) -> None:
        """Добавляет товары в корзину."""
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    @allure.step("Оформление заказа с данными: {first_name} {last_name}, {postal_code}")
    def checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Запускает процесс оформления заказа с указанными данными покупателя."""
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение текста общей суммы заказа")
    def get_total_text(self) -> str:
        """Получает текст с общей суммой заказа."""
        total = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        return total.text

