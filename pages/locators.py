from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn")


class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALL_MESSAGES = (By.CSS_SELECTOR, "div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")