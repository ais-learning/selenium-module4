from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time
from selenium.common.exceptions import NoAlertPresentException # в начале файла



class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.should_go_to_added_to_basket()
        product_name = self.get_product_name()
        self.name_of_product_should_be_in_success_message(product_name)
        product_price = self.get_product_price()
        self.product_price_should_equal_basket_price(product_price)

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented"

    def should_go_to_added_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), "Success message should appear after adding to basket"

    def name_of_product_should_be_in_success_message(self, product_name):
        success_msg_el = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG)
        success_msg = success_msg_el.text
        success_msg_example = product_name + " has been added to your basket."
        # print ("message = ", success_msg)
        # print ("message should be ", success_msg_example)
        assert success_msg == success_msg_example, "Product name should be in success message"

    def product_price_should_equal_basket_price(self, product_price):
        basket_el = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket = basket_el.text
        # print ("basket = ", basket)
        # print ("product_price = ", product_price)
        assert product_price == basket, "Product price should be equal to basket price"

    def solve_quiz_and_get_code(self):
        # *Используйте этот метод в тесте для получения проверочного кода: 
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_el.text

    def get_product_price(self):
        product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_el.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), "Success message should disappear, but not"