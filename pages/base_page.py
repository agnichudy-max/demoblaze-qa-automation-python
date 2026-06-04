# Python logging module
# Used for creating logs during test execution
# Example logs:
# - Opening URL
# - Clicking button
# - Typing text
import logging

# Selenium WebDriverWait
# Used for explicit waits (Explicit waits make Selenium wait for elements
# before interacting with them)
from selenium.webdriver.support.ui import WebDriverWait


# Selenium Expected Conditions
# Provides predefined conditions such as:
# - element clickable
# - element visible
# - alert present
from selenium.webdriver.support import expected_conditions as EC


# Import TIMEOUT value from config file, it keeps wait configuration centralized
from config.config import TIMEOUT


# PyCharm inspection suppression
# Prevents PyCharm warning related to Selenium typing
# This does not affect runtime behavior
# noinspection PyTypeChecker

# Base Page class
# Parent class for all Page Objects
# Every page in the framework inherits from this class
# Purpose:
# - avoid duplicated Selenium code
# - centralize common methods
# - improve maintainability
class BasePage:

    # Constructor
    # Automatically runs when object is created
    # Example:
    # home_page = HomePage(driver)
    def __init__(self, driver):

        # Store browser driver instance
        # Allows page methods to interact with browser
        self.driver = driver

        # Create WebDriverWait object
        # Selenium will wait up to TIMEOUT seconds
        # before throwing an exception
        self.wait = WebDriverWait(driver, TIMEOUT)

        # Create logger object
        # self.__class__.__name__ dynamically uses class name
        # Example:
        # HomePage
        # LoginModal
        self.logger = logging.getLogger(self.__class__.__name__)

    # Open website URL
    # Reusable method for navigation
    def open_url(self, url):

        # Write log message
        self.logger.info(f"Opening URL: {url}")

        # Open browser URL
        self.driver.get(url)

    # Generic click method
    # Reusable method for clicking elements
    # Uses explicit wait before clicking
    def click(self, locator):

        # Log click action
        self.logger.info(f"Clicking: {locator}")

        # Wait until element is clickable
        # then click it
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Generic typing method
    # Reusable method for entering text into fields
    def type_text(self, locator, text):

        # Log typing action
        self.logger.info(f"Typing into: {locator}")

        # Wait until element becomes visible
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        # Clear existing text from field
        element.clear()

        # Type new text into field
        element.send_keys(text)

    # Generic method for retrieving text from element
    # Example:
    # - labels
    # - messages
    # - headers
    def get_text(self, locator):

        # Wait until element is visible
        # then return its text
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # Generic visibility check
    # Returns:
    # True  = visible
    # False = not visible
    def is_visible(self, locator):

        # Wait until element becomes visible
        # then check visibility state
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    # Find multiple elements
    # Returns list of matching elements
    # Example:
    # multiple products on page
    def find_elements(self, locator):

        # * unpacks tuple
        # Example:
        # (By.ID, "login")
        # becomes:
        # find_elements(By.ID, "login")
        return self.driver.find_elements(*locator)

    # Retrieve browser page title
    # Example:
    # "STORE"
    def get_title(self):

        # Return browser title
        return self.driver.title

    # Accept browser alert popup
    # Example:
    # JavaScript alert after adding product to cart
    def accept_alert(self):

        # Wait until alert appears
        # then accept/close it
        self.wait.until(EC.alert_is_present()).accept()

    # Retrieve alert text and close alert
    # Example:
    # "Product added"
    def get_alert_text_and_accept(self):

        # Wait until alert appears
        alert = self.wait.until(EC.alert_is_present())

        # Save alert text
        text = alert.text

        # Accept/close alert
        alert.accept()

        # Return saved alert text
        return text