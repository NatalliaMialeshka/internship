from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):

    SEARCH_ICON = (By.CSS_SELECTOR, "search-modal.header__search")
    SEARCH_FIELD = (By.ID, "Search-In-Modal")
    SEARCH_RESULT = (By.CSS_SELECTOR, "#predictive-search-results-list li a[href*='{TEXT}']")
    SEARCH_FOR_BUTTON = (By.ID, "predictive-search-option-search-keywords")

    def click_on_search(self):
        self.click(*self.SEARCH_ICON)

    def input_search_text(self, text):
        self.input_text(text, *self.SEARCH_FIELD)

    def get_search_text_locator(self, text):
        return [self.SEARCH_RESULT[0], self.SEARCH_RESULT[1].replace("{TEXT}", text)]

    def verify_text_search(self, text):
        locator = self.get_search_text_locator(text)
        self.wait_for_element_appear(*locator)

        self.verify_partial_text(text, *self.SEARCH_FOR_BUTTON)

        self.click(*self.SEARCH_FOR_BUTTON)