import unittest
from selenium import webdriver

from pages.home_page import HomePage


# This is a test class using Python's built-in unittest framework.
# Each method that starts with "test_" will be executed as a test case.
class TestPageTitle(unittest.TestCase):

    # Base URL of the application under test
    BASE_URL = "https://www.demoblaze.com/index.html"

    def setUp(self):
        # setUp() runs before each test method

        # Initialize the browser (Chrome in this case)
        self.driver = webdriver.Chrome()

        # Maximize the browser window (optional, but helps avoid UI issues)
        self.driver.maximize_window()

        # Create an instance of HomePage (Page Object)
        self.home_page = HomePage(self.driver)

        # Open the application in the browser
        self.home_page.open(self.BASE_URL)

    def test_homepage_title_is_store(self):
        # This is a test case

        # Get the actual page title using our page object
        actual_title = self.home_page.get_title()

        # Assert that the title is exactly "STORE"
        # If not, the test will fail
        self.assertEqual("STORE", actual_title)

    def tearDown(self):
        # tearDown() runs after each test method

        # Close the browser and clean up resources
        self.driver.quit()


# This allows the test to be run directly (e.g., python initial_test.py)
if __name__ == "__main__":
    unittest.main()