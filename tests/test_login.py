# Importing Allure reporting library to organize tests inside Allure reports
import allure

# Importing pytest framework for:
#  running tests
#  parametrization
#  fixtures
import pytest

# Importing Faker library, it generates random fake test data
from faker import Faker

# Importing base URL from config file, it keeps configuration centralized
from config.config import BASE_URL

# Importing Page Objects, it contains reusable browser interaction methods
from pages.home_page import HomePage
from pages.login_modal import LoginModal

# Creating Faker object (Used later to generate random test data)
fake = Faker()

# Test class, it groups all login-related tests together
class TestLogin:

    # Valid username used for positive login test
    VALID_USERNAME = "aga-chudy"

    # Valid password used for positive login test
    VALID_PASSWORD = "suntago"

    # Allure report hierarchy
    # Epic   = major business area
    # Feature = specific functionality
    # Story   = exact user scenario
    @allure.epic("Authentication")
    @allure.feature("Login")
    @allure.story("Valid Login")

    # Test case to verify if user can log in with valid credentials
    def test_TC_201_login_with_valid_credentials(self, driver):

        # Create HomePage object
        # Gives access to homepage methods
        home_page = HomePage(driver)

        # Create LoginModal object
        # Gives access to login modal methods
        login_modal = LoginModal(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Opening login popup/modal
        home_page.open_login_modal()

        # Perform login action
        # Uses valid username/password
        login_modal.login(
            self.VALID_USERNAME,
            self.VALID_PASSWORD
        )

        # Verifying welcome message after successful login
        # Example:
        # Welcome aga-chudy
        assert (
            home_page.get_welcome_message()
            == f"Welcome {self.VALID_USERNAME}"
        )

    # Allure report hierarchy
    @allure.epic("Authentication")
    @allure.feature("Login")
    @allure.story("negative Login")

    # Pytest parametrization
    # Instead of writing 3 separate tests,pytest automatically runs this test 3 times
    # three parameters (from lines 89-91) are used
    # Each tuple represents:
    # username, password, expected alert

    @pytest.mark.parametrize(
        "username,password,expected_alert",

        [
            # TC_202_Log_In_With_Non_Existing_User:
            (
                fake.user_name(),
                fake.password(),
                "User does not exist."
            ),

            # TC_203_Log_In_With_Invalid_Password:
            (
                VALID_USERNAME,
                fake.password(),
                "Wrong password."
            ),

            # TC_204_Log_In_With_Missing_Password:
            (
                VALID_USERNAME,
                "",
                "Please fill out Username and Password."
            )
        ]
    )

    # Test case to verify negative login scenarios
    def test_login_negative_scenarios(
        self,

        # Browser fixture from base_page.py
        driver,

        # Parameters are injected automatically by pytest
        username,
        password,
        expected_alert
    ):

        # Create HomePage object
        home_page = HomePage(driver)

        # Create LoginModal object
        login_modal = LoginModal(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Open login popup/modal
        home_page.open_login_modal()

        # Attempt login with test data
        login_modal.login(username, password)

        # Verifying alert message
        # Method also automatically accepts/closes alert
        assert (
            login_modal.get_alert_text_and_accept()
            == expected_alert
        )