from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")
    SUCCESS_REGISTER_MSG = (By.CSS_SELECTOR, ".alert-success .alertinner.wicon")

class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")


class CartPageLocators(object):
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
    # TOTAL_PRICE = (By.CSS_SELECTOR, ".total .price_color")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")