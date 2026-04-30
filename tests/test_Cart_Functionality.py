import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


# This test class verifies cart-related functionality:
# - Viewing product details
# - Adding a product to the cart
# - Verifying cart contents
class TestCartFunctionality(unittest.TestCase):

    # ===== TEST DATA =====
    BASE_URL = "https://www.demoblaze.com/index.html"
    CATEGORY = "Monitors"
    PRODUCT = "Apple monitor 24"

    def setUp(self):
        # Runs before each test

        # Starting browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initializing page objects (Page Object Model)
        self.home_page = HomePage(self.driver)
        self.product_details_page = ProductDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)

        # Opening the application
        self.home_page.open(self.BASE_URL)

    def open_apple_monitor_details_page(self):
        # Helper method to reduce duplicated steps in tests

        # Step 1: Selecting category (e.g., "Monitors")
        self.home_page.select_category(self.CATEGORY)

        # Step 2: Selecting specific product
        self.home_page.select_product(self.PRODUCT)

    # ===== TEST CASES =====

    def test_TC_501_view_product_details_page_load(self):
        # Testing that product details page loads correctly

        self.open_apple_monitor_details_page()

        # Getting actual values from the page
        actual_product_name = self.product_details_page.get_product_name()
        actual_button_text = self.product_details_page.get_add_to_cart_button_text()

        # Validating expected values
        self.assertEqual(self.PRODUCT, actual_product_name)
        self.assertEqual("Add to cart", actual_button_text)

    def test_TC_502_add_product_to_cart_popup_confirmation(self):
        # Testing that adding a product triggers a confirmation alert

        self.open_apple_monitor_details_page()

        # Click "Add to cart"
        self.product_details_page.add_to_cart()

        # getting alert text (browser popup)
        actual_alert = self.product_details_page.get_alert_text()

        # Validate popup message
        self.assertEqual("Product added", actual_alert)

    def test_TC_503_view_cart_with_one_added_product(self):
        # Testing that the cart contains the added product

        self.open_apple_monitor_details_page()

        # Adding product to a cart
        self.product_details_page.add_to_cart()

        # Accepting the confirmation alert (click "OK")
        self.product_details_page.accept_alert()

        # Navigating to cart page
        self.home_page.open_cart()

        # Verify:
        # - Exactly 1 product is in the cart
        # - "Place Order" button is visible
        self.assertEqual(1, self.cart_page.get_number_of_products())
        self.assertTrue(self.cart_page.is_place_order_button_visible())

    def tearDown(self):
        # Running after each test

        # Closing browser
        self.driver.quit()


# Allows running the test file directly
if __name__ == "__main__":
    unittest.main()