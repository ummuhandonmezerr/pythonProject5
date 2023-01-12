from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchPage(BasePage):
    """Class is that including  functions about search page"""

    SEARCH_KEYWORD_CONTROL = (By.CLASS_NAME, "a-color-state")
    SECOND_PAGE = (By.CLASS_NAME, "s-pagination-button")
    THIRD_PRODUCT = (By.TAG_NAME, "h2")
    product = ""

    def __init__(self, driver):
        self.product_page_locators = ProductPage
        super().__init__(driver)

    def keyword_control(self):
        """Check the word if true or not"""

        assert "Samsung" in self.find_element(*self.SEARCH_KEYWORD_CONTROL).text

    def go_to_second_page(self):
        """Go to second page"""

        self.click(*self.SECOND_PAGE)
        assert "page=2" in self.get_url()

    def choose_the_third_product(self):
        """Choose the third product"""

        self.product = self.find_elements(*self.THIRD_PRODUCT)[2].text
        self.click(By.XPATH, "//span[text()='" + self.product + "']")
        self.click(*self.product_page_locators.ADD_TO_LIST_BUTTON)

    def check_product_in_wish_list(self):
        """Check product in wish list"""

        assert self.product == self.find_element(*self.THIRD_PRODUCT).text
