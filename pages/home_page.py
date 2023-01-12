from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """Class is that including functions about homepage"""

    BASE_URL = "https://www.amazon.com/"
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList")
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_WORD = 'samsung'
    SEARCH_CLICK = (By.ID, 'nav-search-submit-text')

    def click_sign_in_button(self):
        """Go to sign in site"""

        self.click(*self.SIGN_IN_BUTTON)

    def search_keyword(self):
        """ Type and search word"""

        self.fill(self.SEARCH_WORD, *self.SEARCH_BOX)
        self.click(*self.SEARCH_CLICK)