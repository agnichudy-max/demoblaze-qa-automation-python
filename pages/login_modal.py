from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# LoginModal represents the login popup/modal on the page.
# It inherits from BasePage, so it has access to:
# - self.driver (browser control)
# - self.wait (explicit waits)
class LoginModal(BasePage):

    # ===== LOCATORS =====
    # These define how we find elements inside the login modal.

    # Input field for username
    USERNAME_INPUT = (By.ID, "loginusername")

    # Input field for password
    PASSWORD_INPUT = (By.ID, "loginpassword")

    # Login button inside the modal
    # The XPath ensures we only target the button within the login modal
    # (important if there are multiple "Log in" buttons on the page)
    LOGIN_BUTTON = (
        By.XPATH,
        "//div[@id='logInModal']//button[normalize-space()='Log in']"
    )

    # ===== ACTION METHODS =====

    def enter_username(self, username):
        # Wait until the username input field is visible
        field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )

        # Clear any existing text (good practice before typing)
        field.clear()

        # Type the username into the field
        field.send_keys(username)

    def enter_password(self, password):
        # Same pattern as username field
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        # Wait until the login button is clickable, then click it
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        # High-level method that performs the full login flow.
        # This is useful in tests to avoid repeating steps.

        # Step 1: Enter username
        self.enter_username(username)

        # Step 2: Enter password
        self.enter_password(password)

        # Step 3: Click login button
        self.click_login()