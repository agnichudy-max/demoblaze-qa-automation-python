# Import Selenium locator strategy class
#
# By allows us to locate elements using:
# - ID
# - XPath
# - CSS Selector
# - Link Text
from selenium.webdriver.common.by import By


# Import BasePage
#
# ProductDetailsPage inherits reusable methods from BasePage, such as:
# - click()
# - get_text()
# - type_text()
from pages.base_page import BasePage


# Product Details Page Object
#
# Represents the product details page
#
# Example:
# Apple monitor 24 page
class ProductDetailsPage(BasePage):

    # Locator for product name/title
    #
    # CSS selector explanation:
    #
    # #tbodyid h2
    #
    # Means:
    # find <h2> element inside element with id="tbodyid"
    #
    # Example:
    # Apple monitor 24
    PRODUCT_NAME = (By.CSS_SELECTOR, "#tbodyid h2")

    # Locator for Add to cart button
    #
    # Link Text locator finds link/button
    # whose visible text is exactly:
    # "Add to cart"
    ADD_TO_CART_BUTTON = (
        By.LINK_TEXT,
        "Add to cart"
    )

    # Returns product name text
    #
    # Example:
    # "Apple monitor 24"
    def get_product_name(self):

        # get_text() comes from BasePage
        return self.get_text(self.PRODUCT_NAME)

    # Clicks Add to cart button
    def add_to_cart(self):

        # click() comes from BasePage
        self.click(self.ADD_TO_CART_BUTTON)

    # Returns Add to cart button text
    #
    # Example:
    # "Add to cart"
    def get_add_to_cart_button_text(self):

        # get_text() comes from BasePage
        return self.get_text(self.ADD_TO_CART_BUTTON)