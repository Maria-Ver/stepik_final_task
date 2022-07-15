from .base_page import BasePage
from .locators import LoginPageLocators

login_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        pass_conf_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        pass_conf_field.send_keys(password)
        register_btn.click()
