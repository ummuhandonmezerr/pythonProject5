import unittest

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    base_url = "http://www.amazon.com/"

    def setUp(self):
        self.home_page_locators = HomePage
        option = Options()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        # self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 10)