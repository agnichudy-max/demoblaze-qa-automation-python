from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# ProductDetailsPage represents the page shown when a user clicks on a product.
# It displays product info (name, price) and actions (like "Add to cart").
class ProductDetailsPage(BasePage):

    # ===== LOCATORS =====

    # The product name (a heading inside the product details section)
    PRODUCT_NAME = (By.CSS_SELECTOR, "#tbodyid h2")

    # The "Add to cart" button (found by its visible link text)
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to cart")

    # ===== DATA / QUERY METHODS =====

    def get_product_name(self):
        # Waits until the product name is visible on the page
        element = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        )

        # Returns the product name text (e.g., "Samsung galaxy s6")
        return element.text

    def get_add_to_cart_button_text(self):
        # Waits until the "Add to cart" button is visible
        element = self.wait.until(
            EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON)
        )

        # Returns the button text (useful for validation in tests)
        return element.text

    # ===== ACTION METHODS =====

    def add_to_cart(self):
        # Waits until the "Add to cart" button is clickable
        # (visible + enabled), then clicks it
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()