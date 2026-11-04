from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page() # Переходим в корзину
    basket_page = BasketPage(browser, browser.current_url) # Инициализируем страницу корзины
    basket_page.should_be_empty_basket() # Проверяем, что товаров нет
    basket_page.should_be_empty_basket_text() # Проверяем, что есть текст о пустоте
@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страниц
    page.add_to_basket()
    page.should_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_to_basket() # Добавляем товар
    page.should_not_be_success_message() # Проверяем, что сообщения нет

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open() # Открываем страницу, ничего не добавляем
    page.should_not_be_success_message() # Проверяем, что сообщения нет
@pytest.mark.need_review
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_to_basket() # Добавляем товар
    page.should_disappear_success_message() # Проверяем, что сообщение исчезло
