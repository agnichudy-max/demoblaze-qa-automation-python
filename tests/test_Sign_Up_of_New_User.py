import unittest
from selenium import webdriver
from faker import Faker
from pages.home_page import HomePage
from pages.signup_modal import SignUpModal

# This test class verifies signup validation scenarios:
# - Empty input
# - Missing username
# - Missing password
class TestSignUpOfNewUser(unittest.TestCase):

    # ===== TEST DATA =====
    BASE_URL = "https://www.demoblaze.com/index.html"

    def setUp(self):
        # Runs before each test

        # Start browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initialize page objects
        self.home_page = HomePage(self.driver)
        self.signup_modal = SignUpModal(self.driver)

        # generating random data for testing
        self.fake = Faker()

        # Open the application
        self.home_page.open(self.BASE_URL)

    # ===== TEST CASES =====

    def test_TC_105_signup_with_empty_username_and_password(self):
        # Test signup with both fields empty

        self.home_page.open_signup_modal()

        # trying signup with empty values
        self.signup_modal.signup("", "")

        # getting alert message
        actual_alert = self.signup_modal.get_alert_text()

        # Validating expected message in the popup
        self.assertEqual(
            "Please fill out Username and Password.",
            actual_alert
        )

    def test_TC_106_signup_with_missing_password(self):
        # Test signup with username but no password

        self.home_page.open_signup_modal()

        # Generating random username
        random_username = self.fake.user_name()

        # Leave password empty
        self.signup_modal.signup(random_username, "")

        # getting alert message
        actual_alert = self.signup_modal.get_alert_text()

        # Validate expected message in the popup
        self.assertEqual(
            "Please fill out Username and Password.",
            actual_alert
        )

    def test_TC_107_signup_with_missing_username(self):
        # Test signup with password but no username

        self.home_page.open_signup_modal()

        # Generating random password
        random_password = self.fake.password()

        # Leave username empty
        self.signup_modal.signup("", random_password)

        # getting alert message
        actual_alert = self.signup_modal.get_alert_text()

        # Validating expected message in the popup
        self.assertEqual(
            "Please fill out Username and Password.",
            actual_alert
        )

    def tearDown(self):
        # Runs after each test

        # Close browser
        self.driver.quit()

# Allows running the test file directly
if __name__ == "__main__":
    unittest.main()