# Import Selenium locator strategy class
# By allows us to locate elements using:
# - ID
# - XPath
# - CSS Selector
# - Link Text
from selenium.webdriver.common.by import By

# Import BasePage
# LoginModal inherits reusable methods from BasePage, such as:
# - click()
# - type_text()
# - get_text()
from pages.base_page import BasePage

# Login Modal Page Object
# Represents the login popup/modal window
class LoginModal(BasePage):

    # Locator for username input field
    # HTML example:
    # <input id="loginusername">
    USERNAME_INPUT = (By.ID, "loginusername")

    # Locator for password input field
    # HTML example:
    # <input id="loginpassword">
    PASSWORD_INPUT = (By.ID, "loginpassword")

    # Locator for Login button inside login modal
    # XPath explanation:
    # //div[@id='logInModal']
    # -> find div with id="logInModal"
    # //button[normalize-space()='Log in']
    # -> find button whose visible text is "Log in"
    LOGIN_BUTTON = (
        By.XPATH,
        "//div[@id='logInModal']//button[normalize-space()='Log in']"
    )

    # Login action method
    # Combines all login steps into one reusable method
    # Example:
    # login("user", "password")
    def login(self, username, password):

        # Type username into username field
        # type_text() comes from BasePage
        self.type_text(self.USERNAME_INPUT, username)

        # Type password into password field
        self.type_text(self.PASSWORD_INPUT, password)

        # Click Login button

        # click() comes from BasePage
        self.click(self.LOGIN_BUTTON)