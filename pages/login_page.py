from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_TEXT = "ummuhandnmzr@gmail.com"
    PASSWORD_TEXT = "123456"
    EMAIL = (By.NAME, 'email')
    EMAIL_SUBMIT = (By.ID, 'continue')
    PASSWORD = (By.NAME, 'password')
    SIGN_IN_SUBMIT = (By.ID, 'signInSubmit')

    def sign_in(self):
        self.fill(self.EMAIL_TEXT, *self.EMAIL)
        self.click(*self.EMAIL_SUBMIT)
        self.fill(self.PASSWORD_TEXT, *self.PASSWORD)
        self.click(*self.SIGN_IN_SUBMIT)
