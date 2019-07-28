from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_FORMSET), \
            "Block with items to buy should not be present in empty cart"

    def should_be_empty_cart_message(self):
        empty_cart_msg_el = self.browser.find_element(*CartPageLocators.EMPTY_BASKET_MSG)
        empty_cart_msg = empty_cart_msg_el.text
        print("empty_cart_msg  ", empty_cart_msg)
        assert empty_cart_msg == "Your basket is empty. Continue shopping", "Should be message Your basket is empty"
