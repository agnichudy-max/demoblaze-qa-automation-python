import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.order_modal import OrderModal


# This test class verifies the full payment (purchase) flow:
# - Opening the order form
# - Validating form errors
# - Completing a purchase successfully
class TestPaymentFunctionality(unittest.TestCase):

    # ===== TEST DATA =====
    BASE_URL = "https://www.demoblaze.com/index.html"
    CATEGORY = "Monitors"
    PRODUCT = "Apple monitor 24"

    def setUp(self):
        # Runs before each test

        # Starting browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initializing page objects
        self.home_page = HomePage(self.driver)
        self.product_page = ProductDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.order_modal = OrderModal(self.driver)

        # Opening the application
        self.home_page.open(self.BASE_URL)

    # ===== HELPER METHOD =====

    def add_product_to_cart(self):
        # Reusable precondition for multiple tests:
        # Adding a product to the cart and navigates to cart page

        # Step 1: Navigating to product
        self.home_page.select_category(self.CATEGORY)
        self.home_page.select_product(self.PRODUCT)

        # Step 2: Adding product to cart
        self.product_page.add_to_cart()

        # Accepting confirmation alert
        self.product_page.accept_alert()

        # Step 3: Going to cart page
        self.home_page.open_cart()

    # ===== TEST CASES =====

    def test_TC_601_open_order_form_from_cart(self):
        # Test that clicking "Place Order" opens the order modal

        self.add_product_to_cart()

        # Click "Place Order"
        self.cart_page.click_place_order()

        # Verifying that the modal is visible
        self.assertTrue(self.order_modal.is_visible())

    def test_TC_602_validate_empty_purchase_form_error_message(self):
        # Testing validation when submitting empty order form

        self.add_product_to_cart()

        self.cart_page.click_place_order()

        # Clicking purchase without filling required fields
        self.order_modal.click_purchase()

        # Getting popup message
        alert_text = self.order_modal.get_alert_text()

        # Validating expected error message
        self.assertEqual("Please fill out Name and Creditcard.", alert_text)

    def test_TC_603_complete_purchase_with_name_and_card(self):
        # Testing successful purchase flow

        self.add_product_to_cart()

        # Getting total price from cart page
        cart_total = self.cart_page.get_total_price()

        # Opening order modal
        self.cart_page.click_place_order()

        # Verifying total price inside modal matches cart total
        modal_total = self.order_modal.get_total_price()
        self.assertEqual(f"Total: {cart_total}", modal_total)

        # Filling in purchase form
        self.order_modal.enter_name("aga-chudy")
        self.order_modal.enter_card("123456")

        # Submitting purchase
        self.order_modal.click_purchase()

        # Capturing success popup text
        popup_text = self.order_modal.get_success_popup_text()

        # Validating that correct amount appears in confirmation
        self.assertIn(f"Amount: {cart_total} USD", popup_text)

    def tearDown(self):
        # Runs after each test

        # Closing browser
        self.driver.quit()


# Allows running the test file directly
if __name__ == "__main__":
    unittest.main()