from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# SignUpModal represents the registration (sign up) popup/modal.
# It follows the same structure as LoginModal, which is good for consistency.
class SignUpModal(BasePage):

    # ===== LOCATORS =====

    # Input field for new username
    USERNAME_INPUT = (By.ID, "sign-username")

    # Input field for new password
    PASSWORD_INPUT = (By.ID, "sign-password")

    # "Sign up" button inside the modal
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(),'Sign up')]")

    # ===== ACTION METHODS =====

    def enter_username(self, username):
        # Wait until the username field is visible
        field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )

        # Clear any existing value (important for test stability)
        field.clear()

        # Enter the username
        field.send_keys(username)

    def enter_password(self, password):
        # Same pattern as username field
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)

    def click_signup(self):
        # Wait until the "Sign up" button is clickable, then click it
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_BUTTON)
        ).click()

    def signup(self, username, password):
        # High-level method that performs the full signup flow.
        # This avoids repeating steps in your tests.

        # Step 1: Enter username
        self.enter_username(username)

        # Step 2: Enter password
        self.enter_password(password)

        # Step 3: Click signup button
        self.click_signup()