from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):

    RESULT_FOUND = (By.ID, "ProductCount")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div.predictive-search__item-content span.h4")

    def verify_search_result(self, text):
        self.verify_partial_text(text, *self.RESULT_FOUND)

    def click_on_product(self):
        self.click(*self.FIRST_PRODUCT)

