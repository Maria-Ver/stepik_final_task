from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    page_name = ''
    page_price = ''

    def find_product_name_on_page(self):
        self.page_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text

    def find_product_price_on_page(self):
        self.page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text

    def should_add_product_to_basket(self):
        self.find_product_name_on_page()
        self.find_product_price_on_page()
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def is_name_in_msgs(self, ):
        messages = self.browser.find_elements(*ProductPageLocators.ALL_MESSAGES)
        for msg in messages:
            if msg.text == self.page_name:
                return True
        return False

    def is_price_in_msgs(self):
        messages = self.browser.find_elements(*ProductPageLocators.ALL_MESSAGES)
        for msg in messages:
            if msg.text == self.page_price:
                return True
        return False

    def should_names_be_same(self):
        assert self.is_name_in_msgs(), f"Name on page: ({self.page_name}) is not in message)"

    def should_price_be_same(self):
        assert self.is_price_in_msgs(), f"Price on page: ({self.page_price}) is not in message"

    def should_product_is_added(self):
        self.should_names_be_same()
        self.should_price_be_same()
