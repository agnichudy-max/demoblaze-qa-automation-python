# Import Allure reporting library
#
# Used to organize tests inside Allure reports
import allure


# Import BASE_URL from config file
#
# Keeps configuration centralized
from config.config import BASE_URL


# Import HomePage Page Object
#
# Page Objects contain reusable UI interaction methods
from pages.home_page import HomePage


# Test class
#
# Groups all category-related tests together
class TestDisplayingCategoryFunctionality:

    # Product category used in tests
    CATEGORY = "Monitors"

    # Expected products visible in Monitors category
    #
    # These are the expected results used for validation
    EXPECTED_MONITORS = [
        "Apple monitor 24",
        "ASUS Full HD"
    ]

    # Allure report hierarchy
    #
    # Epic   = large business area
    # Feature = specific functionality
    # Story   = exact user scenario
    @allure.epic("Product Category")
    @allure.feature("Category Monitor")
    @allure.story("Show page")

    # Test case
    #
    # Verifies:
    # - Monitors category page opens correctly
    # - Correct products are displayed
    def test_TC_401_open_monitors_category_page(self, driver):

        # Create HomePage object
        #
        # Gives access to homepage methods
        home_page = HomePage(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Click "Monitors" category
        home_page.select_category(self.CATEGORY)

        # Retrieve visible product names from page
        actual_products = home_page.get_visible_product_names()

        # Verify exactly 2 products are displayed
        assert len(actual_products) == 2

        # Verify displayed products match expected products
        #
        # set() ignores ordering differences
        #
        # Example:
        # ["A", "B"] == ["B", "A"]
        assert set(actual_products) == set(self.EXPECTED_MONITORS)

    # Allure report hierarchy
    @allure.epic("Product Category")
    @allure.feature("Category Monitor")
    @allure.story("Pagination button visible")

    # Test case
    #
    # Verifies pagination buttons are visible
    # in the Monitors category page
    def test_TC_402_verify_pagination_buttons_visible(self, driver):

        # Create HomePage object
        home_page = HomePage(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Open Monitors category
        home_page.select_category(self.CATEGORY)

        # Verify Previous button is visible
        assert home_page.is_previous_button_visible()

        # Verify Next button is visible
        assert home_page.is_next_button_visible()