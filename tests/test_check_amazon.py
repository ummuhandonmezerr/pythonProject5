from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.wish_list_page import WishListPage
from tests.base_test import BaseTest


class TestCheckAmazon(BaseTest):
    """Test case is :
    1. Go to http://www.amazon.com and confirm with assertion that the homepage is opened.
    2. Open the Login screen and login with a user (if you have a previous membership to the site, it can be.)
    3. Type 'samsung' in the Search field at the top of the screen and click the search button.
    4. On the next page, it will be confirmed that there is a result for Samsung.
    5. Clicking on the 2nd page of the search results will confirm that the 2nd page is currently displayed on the opened page.
    6. Click the 'Add to List' button in the 3rd product from the top.
    7. By clicking on the 'List' link at the top of the screen, the Wish list will be selected.
    8. On the page that opens, it will be confirmed that the product that has been tracked on the previous page is found.
    9. By clicking the 'Delete' button next to this favorite product, it will be removed from my favourites.
    10. On page , it will be confirmed that this product is no longer favorites."""

    def test(self):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        wish_list_page = WishListPage(self.driver)

        """Go to Home Page and confirm"""
        assert self.home_page_locators.BASE_URL == base_page.get_url()
        """Login"""
        home_page.click_sign_in_button()
        """The user is logged in."""
        login_page.sign_in()
        """Write samsung into Search Box and search."""
        home_page.search_keyword()
        """Confirm that Samsung products have arrived."""
        search_page.keyword_control()
        """It goes to page 2 in the search list and confirms that it is on page 2."""
        search_page.go_to_second_page()
        """Click the Add To List button in the 3rd product on page 2."""
        search_page.choose_the_third_product()
        """ View wishlist."""
        product_page.add_to_wish_list()
        """Confirm if the item is correct in the wishlist."""
        search_page.check_product_in_wish_list()
        """Delete product from Wish List."""
        wish_list_page.remove_product_in_wish_list()
        """Confirm that the product has been deleted from the wishlist."""
        wish_list_page.is_the_wish_list_empty()


    def tearDown(self):
        self.driver.close()