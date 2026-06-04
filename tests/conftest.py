# Python module used for creating logs
#
# Logs help us understand what happens during test execution
#
# Example:
# 2025-08-16 | INFO | HomePage | Clicking login button
import logging


# Python module used for:
# - creating folders
# - building file paths
# - interacting with the operating system
import os


# Python module used for retrieving system information
#
# Example:
# - operating system
# - Python version
import platform


# Allure reporting library
#
# Used for:
# - attaching screenshots
# - generating reports
# - adding metadata to reports
import allure


# Pytest testing framework
#
# Used for:
# - fixtures
# - hooks
# - running tests
import pytest


# Selenium WebDriver
#
# Used to automate browser interactions
from selenium import webdriver


# Chrome browser configuration options
#
# Lets us customize how Chrome starts
from selenium.webdriver.chrome.options import Options


# Import project configuration values
#
# BASE_URL       = application URL
# HEADLESS       = determines if browser runs headless
# SCREENSHOT_DIR = screenshot folder name
from config.config import (
    BASE_URL,
    HEADLESS,
    SCREENSHOT_DIR
)


# Pytest fixture
#
# Fixtures are reusable setup/cleanup methods
#
# Any test that uses "driver"
# automatically receives this browser instance
@pytest.fixture
def driver(request):

    # Configure logging format and level
    #
    # INFO means informational logs are displayed
    logging.basicConfig(

        level=logging.INFO,

        # Log format explanation:
        #
        # %(asctime)s   = timestamp
        # %(levelname)s = INFO / ERROR / WARNING
        # %(name)s      = logger name
        # %(message)s   = actual message
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )
    )

    # Create Chrome options object
    #
    # This allows browser customization
    options = Options()

    # Run browser in headless mode if enabled
    #
    # Headless = browser runs in background
    # without visible UI
    if HEADLESS:
        options.add_argument("--headless=new")

    # Set browser window size
    #
    # Important because websites behave differently
    # depending on screen resolution
    options.add_argument("--window-size=1920,1080")

    # Linux/Docker stability option
    options.add_argument("--no-sandbox")

    # Prevent memory-related crashes in Linux
    options.add_argument("--disable-dev-shm-usage")

    # Disable GPU acceleration
    #
    # Improves stability in headless mode
    options.add_argument("--disable-gpu")

    # Start Chrome browser with configured options
    driver = webdriver.Chrome(options=options)

    # Store browser instance inside pytest node
    #
    # This allows hooks to access browser later
    request.node.driver = driver

    # Yield sends browser instance to the test
    #
    # Everything BEFORE yield = setup
    # Everything AFTER yield  = teardown
    yield driver

    # Close browser after test finishes
    driver.quit()


# Pytest hook
#
# Hooks let us interact with pytest lifecycle events
#
# This hook runs after every test execution
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    # Run actual test first
    outcome = yield

    # Retrieve test result object
    report = outcome.get_result()

    # report.when values:
    #
    # "setup"    = before test starts
    # "call"     = actual test body
    # "teardown" = cleanup phase
    #
    # We only want screenshots when:
    # - actual test body failed
    if report.when == "call" and report.failed:

        # Retrieve browser instance from pytest node
        driver = getattr(item, "driver", None)

        # Continue only if browser exists
        if driver:

            # Create screenshots folder if missing
            os.makedirs(
                SCREENSHOT_DIR,
                exist_ok=True
            )

            # Build screenshot file path
            #
            # Example:
            # screenshots/test_login_failed.png
            screenshot_path = os.path.join(
                SCREENSHOT_DIR,
                f"{item.name}.png"
            )

            # Save screenshot to file
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to Allure report
            allure.attach.file(

                # Screenshot file path
                screenshot_path,

                # Name shown in report
                name="Failure screenshot",

                # File type
                attachment_type=allure.attachment_type.PNG
            )


# Pytest session hook
#
# Runs once after ALL tests have finished
#
# Purpose:
# Automatically create environment information
# for the Allure report
def pytest_sessionfinish(session):

    # Retrieve Allure results directory
    #
    # If --alluredir is not provided,
    # default to "allure-results"
    alluredir = (
        session.config.getoption("--alluredir")
        or "allure-results"
    )

    # Create allure-results folder if missing
    os.makedirs(alluredir, exist_ok=True)

    # Build full path to environment file
    environment_file = os.path.join(
        alluredir,
        "environment.properties"
    )

    # Open/create environment.properties file
    #
    # "w" means write mode
    #
    # encoding="utf-8"
    # ensures proper text encoding
    with open(
        environment_file,
        "w",
        encoding="utf-8"
    ) as file:

        # Write browser information
        file.write("Browser=Chrome\n")

        # Write environment name
        file.write("Environment=QA\n")

        # Write application URL
        file.write(f"BaseUrl={BASE_URL}\n")

        # Write framework information
        file.write("Framework=Pytest + Selenium\n")

        # Write operating system
        #
        # Example:
        # Windows
        # Linux
        file.write(
            f"OperatingSystem={platform.system()}\n"
        )

        # Write Python version
        file.write(
            f"PythonVersion={platform.python_version()}\n"
        )

        # Write headless mode status
        #
        # Example:
        # Headless=True
        file.write(f"Headless={HEADLESS}\n")