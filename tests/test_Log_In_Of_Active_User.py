import unittest
from selenium import webdriver
from faker import Faker
from pages.home_page import HomePage
from pages.login_modal import LoginModal


# This test class verifies login functionality for different scenarios:
# - Valid login
# - Non-existing user
# - Wrong password
# - Missing input
# - Special character input
class TestLoginOfActiveUser(unittest.TestCase):

    # ===== TEST DATA =====
    BASE_URL = "https://www.demoblaze.com/index.html"

    # Valid credentials (existing user in the system)
    VALID_USERNAME = "aga-chudy"
    VALID_PASSWORD = "suntago"

    def setUp(self):
        # Runs before each test

        # Start browser
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Initialize page objects
        self.home_page = HomePage(self.driver)
        self.login_modal = LoginModal(self.driver)

        # Faker is used to generate random test data
        # This helps avoid hardcoding values and improves test coverage
        self.fake = Faker()

        # Open the application
        self.home_page.open(self.BASE_URL)

    # ===== TEST CASES =====

    def test_TC_201_login_with_valid_credentials(self):
        # Test successful login with valid username and password

        self.home_page.open_login_modal()

        # Perform login using valid credentials
        self.login_modal.login(self.VALID_USERNAME, self.VALID_PASSWORD)

        # Get welcome message after login
        actual_message = self.home_page.get_welcome_message()

        # Verify correct welcome message is displayed
        self.assertEqual(f"Welcome {self.VALID_USERNAME}", actual_message)

    def test_TC_202_login_with_non_existing_user(self):
        # Test login attempt with a user that does not exist

        self.home_page.open_login_modal()

        # Generate random credentials
        random_username = self.fake.user_name()
        random_password = self.fake.password()

        self.login_modal.login(random_username, random_password)

        # Capture alert message
        actual_alert = self.login_modal.get_alert_text()

        # Validate error message
        self.assertEqual("User does not exist.", actual_alert)

    def test_TC_203_login_with_invalid_password(self):
        # Test login with correct username but wrong password

        self.home_page.open_login_modal()

        # Generate random password
        random_password = self.fake.password()

        self.login_modal.login(self.VALID_USERNAME, random_password)

        # Capture alert message
        actual_alert = self.login_modal.get_alert_text()

        # Validate error message
        self.assertEqual("Wrong password.", actual_alert)

    def test_TC_204_login_with_missing_password(self):
        # Test login when username is correct but password field is empty

        self.home_page.open_login_modal()

        self.login_modal.login(self.VALID_USERNAME, "")

        # Capture alert message
        actual_alert = self.login_modal.get_alert_text()

        # Validate validation message
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