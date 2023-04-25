from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    POP_UP = (By.CSS_SELECTOR, "button.popup-close")

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')

    def close_pop_up(self):
        self.wait_for_element_appear(self.POP_UP).click()