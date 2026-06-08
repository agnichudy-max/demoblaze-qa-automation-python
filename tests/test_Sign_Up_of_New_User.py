# Import Allure reporting library
# Used to organize tests inside Allure reports
import allure

# Import pytest framework
# Used for:
# - running tests
# - parametrization
# - fixtures
import pytest

# Import Faker library
# Faker generates random fake test data

# Examples:
# - usernames
# - passwords
# - names
from faker import Faker

# Import base URL from config file
# Keeps configuration centralized
from config.config import BASE_URL

# Import Page Objects
# Page Objects contain reusable browser interaction methods
from pages.home_page import HomePage
from pages.signup_modal import SignUpModal

# Create Faker object
# Used later to generate random test data
fake = Faker()

# Test class
# Groups all signup-related tests together
class TestSignup:

    # Pytest parametrization

    # Instead of writing multiple separate tests,
    # pytest automatically runs this test multiple times

    # Each tuple contains:
    # username, password, expected alert message
    @pytest.mark.parametrize(
        "username,password,expected_alert",

        [
            # Scenario 1:
            # TC_105_Sign_Up_With_Empty_Username_And_Password
            (
                "",
                "",
                "Please fill out Username and Password."
            ),

            # Scenario 2:
            # TC_106_Sign_Up_With_Missing_Password
            (
                fake.user_name(),
                "",
                "Please fill out Username and Password."
            ),

            # Scenario 3:
            # TC_107_Sign_Up_With_Missing_Username
            (
                "",
                fake.password(),
                "Please fill out Username and Password."
            )
        ]
    )

    # Allure report hierarchy

    # Epic   = major business area
    # Feature = specific functionality
    # Story   = exact user scenario
    @allure.epic("Authentication")
    @allure.feature("Signup")
    @allure.story("Invalid signup")

    # Test case
    # Verifies invalid signup scenarios
    def test_signup_negative_scenarios(
        self,

        # Browser fixture from conftest.py
        driver,

        # Parameters injected automatically by pytest
        username,
        password,
        expected_alert
    ):

        # Create HomePage object

        # Gives access to homepage methods
        home_page = HomePage(driver)

        # Create Signup Modal object

        # Gives access to signup modal methods
        signup_modal = SignUpModal(driver)

        # Open website
        home_page.open_url(BASE_URL)

        # Open signup popup/modal
        home_page.open_signup_modal()

        # Attempt signup using test data
        signup_modal.signup(username, password)

        # Verify browser alert message

        # Method also automatically accepts/closes alert
        assert (
            signup_modal.get_alert_text_and_accept()
            == expected_alert
        )