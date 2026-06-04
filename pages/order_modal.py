from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# OrderModal represents the purchase/order popup shown when placing an order.
# It inherits functionality from BasePage.
class OrderModal(BasePage):

    # ===== LOCATORS =====

    # The modal container itself (used to check if it's visible)
    MODAL = (By.ID, "orderModal")

    # Button to confirm the purchase
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")

    # Element showing the total price inside the modal
    TOTAL_PRICE = (By.ID, "totalm")

    # Input fields inside the form
    NAME_INPUT = (By.ID, "name")
    CARD_INPUT = (By.ID, "card")

    # Success popup shown after completing purchase
    # (this uses a CSS class from SweetAlert library)
    SUCCESS_POPUP = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")

    # ===== STATE / VISIBILITY =====

    def is_visible(self):
        # Waits until the modal is visible on the page
        # Returns True if it is displayed
        return self.wait.until(
            EC.visibility_of_element_located(self.MODAL)
        ).is_displayed()

    # ===== DATA / QUERY METHODS =====

    def get_total_price(self):
        # Waits until the total price is visible
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_PRICE)
        )

        # Returns the price text (e.g., "790")
        return element.text

    # ===== FORM INPUT METHODS =====

    def enter_name(self, name):
        # Waits for the name input field to be visible
        field = self.wait.until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )

        # Clears existing value and enters new name
        field.clear()
        field.send_keys(name)

    def enter_card(self, card):
        # Same pattern for card input field
        field = self.wait.until(
            EC.visibility_of_element_located(self.CARD_INPUT)
        )
        field.clear()
        field.send_keys(card)

    # ===== ACTION METHODS =====

    def click_purchase(self):
        # Waits until the purchase button is clickable, then clicks it
        self.wait.until(
            EC.element_to_be_clickable(self.PURCHASE_BUTTON)
        ).click()

    def get_success_popup_text(self):
        # Waits for the success popup to appear after purchase
        popup = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_POPUP)
        )

        # Returns the full text shown in the popup
        return popup.text