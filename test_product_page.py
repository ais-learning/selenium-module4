# 4.3 Улучшаем дизайн тестов
# Шаг 2. Задание: добавление в корзину со страницы товара
import pytest
from pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209"

# links = [
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

links = [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()

# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_add_to_basket()
#     page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_add_to_basket()
#     page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()