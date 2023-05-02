from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://shop.cureskin.com/'

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Checking by locator {locator}. Expected text {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def verify_count_of_links(self, expected_num, *locator):
        actual_num = self.driver.find_elements(*locator)
        assert int(expected_num) == len(actual_num), \
            f'Checking by locator {locator}. Expected {expected_num}, but got {actual_num}'

    def click_through_links_n_verify_text(self, *locator, name_locator):
        all_links = self.find_elements(*locator)
        for i in range(len(all_links)):
            self.link_to_click = self.find_elements(*locator)[i]
            self.link_text = self.link_to_click.text
            self.link_to_click.click()
            self.verify_partial_text(self.link_text, *name_locator)

    def select_different_colors_for_product_n_verify_name(self, *locator, current_color, expected_colors):
        all_color_options = self.find_elements(*locator)
        actual_colors = []
        for color in all_color_options:
            color.click()
            self.current_color = self.find_element(*current_color).text
            actual_colors += [self.current_color]

        assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'


