from .base_page import BasePage
from .locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "Login url does not contain login-word"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.click()
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_input1.click()
        password_input1.send_keys(password)
        password_input2.click()
        password_input2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTER_MSG), "Success register message is not presented"