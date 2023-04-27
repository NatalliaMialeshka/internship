from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#product-form-template--17185951023421__main div.product-form__buttons button[name='add']")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")

    def click_add_to_cart_button(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_on_view_cart_button(self):
        self.click(*self.VIEW_CART_BTN)