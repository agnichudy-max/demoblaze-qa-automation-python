# Import Selenium locator strategy class
#
# By lets us locate elements using:
# - ID
# - XPath
# - CSS selector
# - link text
from selenium.webdriver.common.by import By


# Import BasePage
#
# CartPage inherits reusable methods from BasePage, such as:
# - click()
# - get_text()
# - is_visible()
# - find_elements()
from pages.base_page import BasePage


# Cart Page Object
#
# Represents the cart page in the application
class CartPage(BasePage):

    # Locator for all product rows in the cart table
    #
    # "#tbodyid tr" means:
    # find all table rows inside the element with id="tbodyid"
    PRODUCT_ROWS = (
        By.CSS_SELECTOR,
        "#tbodyid tr"
    )

    # Locator for the Place Order button
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    # Locator for the total price displayed in the cart
    TOTAL_PRICE = (By.ID, "totalp")

    # Returns the number of products currently shown in the cart
    def get_number_of_products(self):

        # find_elements() returns a list
        # len() counts how many elements are in that list
        return len(self.find_elements(self.PRODUCT_ROWS))

    # Checks if the Place Order button is visible
    def is_place_order_button_visible(self):

        # is_visible() comes from BasePage
        return self.is_visible(self.PLACE_ORDER_BUTTON)

    # Clicks the Place Order button
    def click_place_order(self):

        # click() comes from BasePage
        return self.click(self.PLACE_ORDER_BUTTON)

    # Gets the total price text from the cart
    def get_total_price(self):

        # get_text() comes from BasePage
        return self.get_text(self.TOTAL_PRICE)