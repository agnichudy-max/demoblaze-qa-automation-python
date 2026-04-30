from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# CartPage represents the shopping cart page in your application.
# It inherits from BasePage, meaning it reuses shared functionality
# like driver setup and waiting logic.
class CartPage(BasePage):

    # Locators: These define how Selenium finds elements on the page.
    # Using tuples (By.<METHOD>, "selector") is a standard pattern.

    # Finds all rows (<tr>) inside the cart table body (#tbodyid)
    PRODUCT_ROWS = (By.CSS_SELECTOR, "#tbodyid tr")

    # Finds the "Place Order" button using its visible text
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")

    # Finds the element that displays the total price
    TOTAL_PRICE = (By.ID, "totalp")

    def get_number_of_products(self):
        # Waits until all product rows are visible on the page.
        # This ensures the cart has loaded before counting items.
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_ROWS)
        )

        # Returns the number of products in the cart
        return len(products)

    def is_place_order_button_visible(self):
        # Waits until the "Place Order" button is visible
        element = self.wait.until(
            EC.visibility_of_element_located(self.PLACE_ORDER_BUTTON)
        )

        # is_displayed() returns True if the element is visible to the user
        return element.is_displayed()

    def click_place_order(self):
        # Waits until the button is clickable (visible + enabled)
        # This avoids common Selenium errors where elements are not ready
        self.wait.until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        ).click()

    def get_total_price(self):
        # Waits until the total price element is visible
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        )

        # Returns the text value (e.g., "790")
        return element.text