from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """Class is that including base functions"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)

    def find_element(self, *locator):
        """Find element from locators"""

        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        """Find elements of products"""

        return self.driver.find_elements(*locator)

    def get_title(self):
        """Get title of amazon"""

        return self.driver.title

    def get_url(self):
        """Get url of amazon"""

        return self.driver.current_url

    def visibility_element(self, *locator):
        """ Visibility element is that waiting element for being visible"""

        return self.wait.until(ec.visibility_of_element_located(*locator))

    def fill(self, text, *locator):
        """Fill the blank on pages"""

        self.find_element(*locator).send_keys(text)

    def click(self, *locator):
        """Click elements"""

        self.find_element(*locator).click()