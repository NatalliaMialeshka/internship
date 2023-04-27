from pages.main_page import MainPage
from pages.header import Header
from pages.search_result import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_result = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
