import unittest
from selenium import webdriver
from pages.home_page import HomePage

# This test class verifies category display functionality:
# - Correct products are shown when selecting a category
# - Pagination buttons behave correctly based on product count
class TestDisplayingCategoryFunctionality(unittest.TestCase):

    # ===== TEST DATA =====
    # capital letters it is a constant
    BASE_URL = "https://www.demoblaze.com/index.html"
    CATEGORY = "Monitors"

    # Expected products in the "Monitors" category, as a list []
    EXPECTED_MONITORS = [
        "Apple monitor 24",
        "ASUS Full HD",
    ]

    def setUp(self):
        # Runs before each test

        # Starting browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initializing HomePage object
        self.home_page = HomePage(self.driver)

        # Opening the application
        self.home_page.open(self.BASE_URL)

    # ===== TEST CASES =====

    def test_TC_401_open_monitors_category_page(self):
        # Test that selecting the "Monitors" category shows correct products

        # Clicking the category
        self.home_page.select_category(self.CATEGORY)

        # Getting list of visible product names
        actual_product_names = self.home_page.get_visible_product_names()

        # Validating number of products displayed
        self.assertEqual(2, len(actual_product_names))

        # Validating that the correct products are shown (order doesn't matter)
        # Using set() ignores ordering differences
        self.assertEqual(set(self.EXPECTED_MONITORS), set(actual_product_names))

    def test_TC_402_verify_pagination_buttons_not_visible_for_small_product_list(self):
        # Test that pagination buttons are hidden when few products exist

        # Selecting category
        self.home_page.select_category(self.CATEGORY)

        # Verifying "Previous" button is not visible
        self.assertFalse(self.home_page.is_previous_button_visible())

        # Verifying "Next" button is not visible
        self.assertFalse(self.home_page.is_next_button_visible())

    def tearDown(self):
        # Runs after each test

        # Close browser
        self.driver.quit()


# Allows running this file directly
if __name__ == "__main__":
    unittest.main()