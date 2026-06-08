# Import Allure reporting library
#
# Used to organize tests inside Allure reports
import allure


# Import Faker library
#
# Faker generates fake/random test data
#
# Examples:
# - names
# - credit card numbers
from faker import Faker


# Import base URL from config file
#
# Keeps configuration centralized
from config.config import BASE_URL


# Import Page Objects
#
# Page Objects contain reusable browser interaction methods
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.order_modal import OrderModal


# Create Faker object
#
# Used later to generate random payment data
fake = Faker()


# Test class
#
# Groups all payment-related tests together
class TestPaymentFunctionality:

    # Product category used in tests
    CATEGORY = "Monitors"

    # Product used in tests
    PRODUCT = "Apple monitor 24"

    # Helper method
    #
    # Reusable precondition method
    #
    # Steps:
    # 1. Open website
    # 2. Open category
    # 3. Open product
    # 4. Add product to cart
    # 5. Accept popup alert
    # 6. Open cart page
    #
    # This avoids duplicating the same logic in every test
    def add_product_to_cart(self, driver):

        # Create HomePage object
        home_page = HomePage(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Open category
        home_page.select_category(self.CATEGORY)

        # Open product details page
        home_page.select_product(self.PRODUCT)

        # Create Product Details Page object
        product_page = ProductDetailsPage(driver)

        # Add product to cart
        product_page.add_to_cart()

        # Accept popup alert
        #
        # Alert must be closed before continuing
        product_page.accept_alert()

        # Open cart page
        home_page.open_cart()

    # Allure report hierarchy
    #
    # Epic   = large business area
    # Feature = specific functionality
    # Story   = exact scenario
    @allure.epic("Payment Functionality")
    @allure.feature("Open Order")
    @allure.story("Open order from cart")

    # Test case
    #
    # Verifies order modal opens correctly
    def test_TC_601_open_order_form_from_cart(self, driver):

        # Add product to cart
        self.add_product_to_cart(driver)

        # Create Cart Page object
        cart_page = CartPage(driver)

        # Click Place Order button
        cart_page.click_place_order()

        # Create Order Modal object
        order_modal = OrderModal(driver)

        # Verify order modal is visible
        assert order_modal.is_visible()

    # Allure report hierarchy
    @allure.epic("Payment Functionality")
    @allure.feature("Purchase")
    @allure.story("Purchase form error message")

    # Test case
    #
    # Verifies error message appears
    # when purchase form is submitted empty
    def test_TC_602_validate_empty_purchase_form_error_message(self, driver):

        # Add product to cart
        self.add_product_to_cart(driver)

        # Create Cart Page object
        cart_page = CartPage(driver)

        # Open order modal
        cart_page.click_place_order()

        # Create Order Modal object
        order_modal = OrderModal(driver)

        # Click Purchase button without filling form
        order_modal.click_purchase()

        # Verify browser alert message
        #
        # Method also automatically accepts/closes alert
        assert (
            order_modal.get_alert_text_and_accept()
            == "Please fill out Name and Creditcard."
        )

    # Allure report hierarchy
    @allure.epic("Payment Functionality")
    @allure.feature("Purchase")
    @allure.story("Purchase with name and card")

    # Test case
    #
    # Verifies successful purchase flow
    def test_TC_603_complete_purchase_with_name_and_card(self, driver):

        # Add product to cart
        self.add_product_to_cart(driver)

        # Create Cart Page object
        cart_page = CartPage(driver)

        # Retrieve total price from cart
        cart_total = cart_page.get_total_price()

        # Open order modal
        cart_page.click_place_order()

        # Create Order Modal object
        order_modal = OrderModal(driver)

        # Verify total price inside order modal
        #
        # Example:
        # Total: 400
        assert (
            order_modal.get_total_price()
            == f"Total: {cart_total}"
        )

        # Enter random fake customer name
        order_modal.enter_name(fake.name())

        # Enter random fake credit card number
        order_modal.enter_card(fake.credit_card_number())

        # Click Purchase button
        order_modal.click_purchase()

        # Retrieve success popup text
        popup_text = order_modal.get_success_popup_text()

        # Verify purchase amount appears in popup
        #
        # Example:
        # Amount: 400 USD
        assert f"Amount: {cart_total} USD" in popup_text