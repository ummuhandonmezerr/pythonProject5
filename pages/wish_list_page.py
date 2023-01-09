from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishListPage(BasePage):

    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.XPATH, "//div[@class = 'a-alert-content' and text()='Deleted']")

    def remove_product_in_wish_list(self):
        self.click(*self.DELETE_BUTTON)

    def is_the_wish_list_empty(self):
        assert "Deleted" == self.visibility_element(self.DELETED_TEXT).text
