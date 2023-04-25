from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):

    RESULT_FOUND = (By.ID, "ProductCount")

    def verify_search_result(self, text):
        self.verify_partial_text(text, *self.RESULT_FOUND)