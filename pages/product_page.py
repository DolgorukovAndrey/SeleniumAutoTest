from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            pass  # если алерта нет — просто идем дальше

    def should_be_success_message(self):
        # Берем текст сообщения (убираем крестик и пробелы по краям)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text.replace("×", "").strip()
        
        # Берем название товара (тоже чистим)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.replace("×", "").strip()
        
        # СТРОГАЯ ПРОВЕРКА: сообщение ДОЛЖНО начинаться с названия товара
        assert success_message.startswith(product_name), f"БАГ! Ожидали '{product_name}', а получили '{success_message}'"
