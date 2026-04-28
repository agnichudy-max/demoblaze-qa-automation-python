from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# BasePage is a common pattern in Selenium (Page Object Model)
# It acts as a parent class for all page classes, so shared functionality is defined in one place

# pycharm inspection is disabled
# noinspection PyTypeChecker
class BasePage:
    def __init__(self, driver):
        # The WebDriver instance (e.g., Chrome, Firefox)
        # This is what controls the browser
        self.driver = driver

        # WebDriverWait allows us to wait for certain conditions before continuing
        # This is important because web pages often load elements asynchronously.
        # Here we set a default timeout of 10 seconds
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        # Navigates the browser to a given URL.
        # Equivalent to typing a URL in the browser and pressing Enter
        self.driver.get(url)

    def get_title(self):
        # Returns the current page title (the text in the browser tab).
        return self.driver.title

    def get_alert_text(self):
        # Waits until a browser alert (popup) appears.
        # EC.alert_is_present() is an expected condition that checks for alerts.
        alert = self.wait.until(EC.alert_is_present())

        # Returns the text shown inside the alert popup.
        return alert.text

    def accept_alert(self):
        # Waits until an alert is present (same as above).
        alert = self.wait.until(EC.alert_is_present())

        # Accepts the alert (equivalent to clicking "OK").
        alert.accept()