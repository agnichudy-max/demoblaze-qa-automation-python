# Import Selenium locator strategy class
# By allows us to locate elements using:
# - ID
# - XPath
# - CSS Selector
# - Link Text
from selenium.webdriver.common.by import By

# Import BasePage
# SignUpModal inherits reusable methods from BasePage, such as:
# - click()
# - type_text()
# - get_text()
from pages.base_page import BasePage

# Signup Modal Page Object
# Represents the signup popup/modal window
class SignUpModal(BasePage):

    # Locator for username input field
    # HTML example:
    # <input id="sign-username">
    USERNAME_INPUT = (By.ID, "sign-username")

    # Locator for password input field
    # HTML example:
    # <input id="sign-password">
    PASSWORD_INPUT = (By.ID, "sign-password")

    # Locator for Sign up button
    # XPath explanation:
    # //button[contains(text(),'Sign up')]
    # Means:
    # find button containing visible text "Sign up"
    SIGNUP_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Sign up')]"
    )

    # Signup action method
    # Combines all signup steps into one reusable method
    # Example:
    # signup("newuser", "password123")
    def signup(self, username, password):

        # Type username into username field
        # type_text() comes from BasePage
        self.type_text(self.USERNAME_INPUT, username)

        # Type password into password field
        self.type_text(self.PASSWORD_INPUT, password)

        # Click Sign up button
        # click() comes from BasePage
        self.click(self.SIGNUP_BUTTON)