# Import Allure reporting library
#
# Used for:
# - test categorization
# - reporting
# - readable test hierarchy
import allure


# Import base URL from config file
#
# Keeps configuration centralized instead of hardcoding URLs
from config.config import BASE_URL


# Import Page Objects
#
# Page Objects contain reusable UI interaction methods
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


# Test class
#
# Groups together all cart-related test cases
class TestCartFunctionality:

    # Product category used in tests
    CATEGORY = "Monitors"

    # Product used in tests
    PRODUCT = "Apple monitor 24"

    # Helper method
    #
    # This avoids duplicating navigation logic
    #
    # Steps:
    # 1. Open homepage
    # 2. Open category
    # 3. Open product page
    def open_product_page(self, driver):

        # Create HomePage object
        #
        # Gives access to homepage methods
        home_page = HomePage(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Click "Monitors" category
        home_page.select_category(self.CATEGORY)

        # Click specific product
        home_page.select_product(self.PRODUCT)

        # Return HomePage object
        #
        # Needed later for cart navigation
        return home_page

    # Allure metadata
    #
    # Creates report structure:
    # Epic -> Feature -> Story
    #
    # Helps organize large test suites visually
    @allure.epic("Product")
    @allure.feature("Product Details")
    @allure.story("Show Product Details")

    # Test case
    #
    # Verifies product details page loads correctly
    def test_TC_501_view_product_details_page_load(self, driver):

        # Open product page using helper method
        self.open_product_page(driver)

        # Create Product Details Page object
        product_page = ProductDetailsPage(driver)

        # Verify product name is correct
        #
        # Expected:
        # Apple monitor 24
        assert (
            product_page.get_product_name()
            == self.PRODUCT
        )

        # Verify Add to cart button text
        assert (
            product_page.get_add_to_cart_button_text()
            == "Add to cart"
        )

    # Allure report categorization
    @allure.epic("Product")
    @allure.feature("Product Details")
    @allure.story("Add to cart")

    # Test case
    #
    # Verifies alert popup after adding product to cart
    def test_TC_502_add_product_to_cart_popup_confirmation(self, driver):

        # Open product page
        self.open_product_page(driver)

        # Create Product Details Page object
        product_page = ProductDetailsPage(driver)

        # Click Add to cart button
        product_page.add_to_cart()

        # Verify alert message
        #
        # Also accepts/closes alert automatically
        assert (
            product_page.get_alert_text_and_accept()
            == "Product added"
        )

    # Allure report categorization
    @allure.epic("Product")
    @allure.feature("Product Details")
    @allure.story("Cart with one product")

    # Test case
    #
    # Verifies cart contains one product after adding it
    def test_TC_503_view_cart_with_one_added_product(self, driver):

        # Open product page
        #
        # Save returned HomePage object
        home_page = self.open_product_page(driver)

        # Create Product Details Page object
        product_page = ProductDetailsPage(driver)

        # Add product to cart
        product_page.add_to_cart()

        # Accept alert popup
        #
        # Alert must be closed before interacting with page again
        product_page.accept_alert()

        # Open cart page
        home_page.open_cart()

        # Create Cart Page object
        cart_page = CartPage(driver)

        # Verify cart contains exactly one product
        assert cart_page.get_number_of_products() == 1

        # Verify Place Order button is visible
        assert cart_page.is_place_order_button_visible()