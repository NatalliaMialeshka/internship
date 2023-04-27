from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class CartPage(Page):

    MINUS_BUTTON = (By.CSS_SELECTOR, "button[name='minus']")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "h2.cart__empty-text")

    def click_on_minus_button(self):
        self.click(*self.MINUS_BUTTON)
        sleep(5)

    def verify_cart_is_empty(self):
        self.verify_text('Your cart is currently empty', *self.EMPTY_CART_TEXT)