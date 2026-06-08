# Import Selenium locator strategy class
#
# By allows us to locate elements using:
# - ID
# - XPath
# - CSS Selector
from selenium.webdriver.common.by import By


# Import BasePage
#
# OrderModal inherits reusable methods from BasePage, such as:
# - click()
# - type_text()
# - get_text()
# - is_visible()
from pages.base_page import BasePage


# Order Modal Page Object
#
# Represents the purchase/order popup modal
class OrderModal(BasePage):

    # Locator for the order modal container
    #
    # HTML example:
    # <div id="orderModal">
    MODAL = (By.ID, "orderModal")

    # Locator for Purchase button
    #
    # XPath explanation:
    #
    # //button[text()='Purchase']
    # -> find button whose visible text is exactly "Purchase"
    PURCHASE_BUTTON = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    # Locator for total price shown in modal
    #
    # Example:
    # Total: 400
    TOTAL_PRICE = (By.ID, "totalm")

    # Locator for customer name input field
    NAME_INPUT = (By.ID, "name")

    # Locator for credit card input field
    CARD_INPUT = (By.ID, "card")

    # Locator for success popup after successful purchase
    #
    # CSS selector explanation:
    #
    # .sweet-alert.showSweetAlert.visible
    #
    # Means:
    # find element containing ALL these classes:
    # - sweet-alert
    # - showSweetAlert
    # - visible
    SUCCESS_POPUP = (
        By.CSS_SELECTOR,
        ".sweet-alert.showSweetAlert.visible"
    )

    # Checks if order modal is visible
    def is_visible(self):

        # super() accesses methods from parent class (BasePage)
        #
        # is_visible() returns True/False
        return super().is_visible(self.MODAL)

    # Returns total price text from modal
    #
    # Example:
    # "Total: 400"
    def get_total_price(self):

        # get_text() comes from BasePage
        return self.get_text(self.TOTAL_PRICE)

    # Enters customer name into name field
    def enter_name(self, name):

        # type_text() comes from BasePage
        self.type_text(self.NAME_INPUT, name)

    # Enters credit card number into card field
    def enter_card(self, card):

        # type_text() comes from BasePage
        self.type_text(self.CARD_INPUT, card)

    # Clicks Purchase button
    def click_purchase(self):

        # click() comes from BasePage
        self.click(self.PURCHASE_BUTTON)

    # Returns success popup text
    #
    # Example:
    # "Thank you for your purchase!"
    def get_success_popup_text(self):

        # get_text() comes from BasePage
        return self.get_text(self.SUCCESS_POPUP)