from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    VIEW_YOUR_LIST_BUTTON = (By.LINK_TEXT, "View Your List")

    def add_to_wish_list(self):
        self.click(*self.VIEW_YOUR_LIST_BUTTON)
