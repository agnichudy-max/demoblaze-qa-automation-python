# Demoblaze QA Automation - Python, Selenium, Pytest and Allure

## Project Overview

This project contains automated UI tests for the Demoblaze e-commerce application:

https://www.demoblaze.com/index.html

The project uses:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Faker
- Allure Reports
- Screenshots on failed tests
- Central configuration
- Pytest fixtures for browser setup and teardown

The purpose of this project is to demonstrate a maintainable automated test framework rather than only a collection of Selenium scripts.

---

## Key Features

- Page Object Model architecture
- Reusable `BasePage`
- Pytest fixtures for setup and teardown
- Data-driven / parameterized tests using `pytest.mark.parametrize`
- Randomized test data using Faker
- Allure reporting
- Screenshot attachment on failed tests
- Configuration file for base URL, timeout, headless mode and screenshot folder
- Setup scripts for Linux and Windows
- Can be run both inside and outside PyCharm

---

## Scope of Testing

The automated tests cover:

- User registration / sign up
- User login
- Product category navigation
- Product details page
- Cart functionality
- Purchase / payment flow

---

## Tech Stack

| Area | Tool |
|---|---|
| Language | Python |
| Test framework | Pytest |
| Browser automation | Selenium WebDriver |
| Browser | Google Chrome |
| Test data | Faker |
| Reporting | Allure |
| Design pattern | Page Object Model |

---

## Project Structure

```text
demoblaze-qa-automation-python/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_details_page.py
│   ├── cart_page.py
│   ├── login_modal.py
│   ├── signup_modal.py
│   └── order_modal.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_signup.py
│   ├── test_Displaying_Category_Functionality.py
│   ├── test_Cart_Functionality.py
│   └── test_Payment_Functionality.py
│
├── screenshots/
├── allure-results/
├── requirements.txt
├── pytest.ini
├── setup_project.sh
├── setup_project_windows.bat
└── README.md
```

---

## Why empty `__init__.py` files are used

The project contains empty `__init__.py` files in folders such as:

```text
config/__init__.py
pages/__init__.py
tests/__init__.py
```

These files are intentionally empty.

They are used because Python treats folders containing `__init__.py` as importable packages. This makes imports more reliable, especially when running tests from different tools such as:

- terminal
- PyCharm
- pytest
- CI/CD pipelines

Example:

```python
from config.config import BASE_URL
from pages.home_page import HomePage
```

Without `__init__.py`, Python may fail with errors such as:

```text
ModuleNotFoundError: No module named 'config'
```

So even though the files are empty, they help Python understand the project structure.

---

## Test Architecture

This project follows the Page Object Model pattern.

### Page Objects

Files in the `pages/` folder represent pages or modal windows in the application.

Examples:

- `HomePage`
- `LoginModal`
- `SignUpModal`
- `CartPage`
- `OrderModal`

Tests do not directly use Selenium locators. Instead, tests call methods from Page Objects.

Example:

```python
home_page.open_login_modal()
login_modal.login(username, password)
```

This makes the tests easier to read and easier to maintain.

---

## BasePage

`BasePage` contains reusable Selenium functionality used by all Page Objects.

Examples:

```python
click(locator)
type_text(locator, text)
get_text(locator)
is_visible(locator)
accept_alert()
get_alert_text_and_accept()
```

This avoids duplicated Selenium code in every Page Object and makes the framework easier to extend.

---

## Configuration

The file `config/config.py` contains shared project settings:

```python
BASE_URL = "https://www.demoblaze.com/index.html"
TIMEOUT = 10
HEADLESS = False
SCREENSHOT_DIR = "screenshots"
```

This avoids hardcoding configuration values throughout the test files.

---

# Installation and Environment Setup

## Option 1: Linux setup script

Use this option on Linux or Ubuntu.

From the project root, run:

```bash
chmod +x setup_project.sh
./setup_project.sh
```

The Linux setup script installs:

- Java
- Node.js
- npm
- Allure CLI
- Python virtual environment
- Selenium
- Pytest
- Faker
- Allure Pytest plugin

After setup, activate the environment:

```bash
source .venv/bin/activate
```

---

## Option 2: Windows setup script

Use this option on Windows.

Open Command Prompt as Administrator in the project root and run:

```cmd
setup_project_windows.bat
```

The Windows setup script installs or configures:

- Python virtual environment
- Selenium
- Pytest
- Faker
- Allure Pytest plugin
- Java
- Node.js
- Allure CLI

If Chocolatey is missing, install it manually first:

https://community.chocolatey.org/install

Then rerun:

```cmd
setup_project_windows.bat
```

---

## Manual setup

If you do not want to use the setup scripts, use the manual setup steps below.

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

# Running Tests

## Important: running outside PyCharm

When running tests from a terminal outside PyCharm, always make sure the virtual environment is activated first.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate.bat
```

Then run pytest with:

```bash
python -m pytest
```

Using `python -m pytest` is recommended because it ensures pytest runs using the Python interpreter from the active virtual environment.

---

## Run all tests

```bash
python -m pytest
```

---

## Run all tests with verbose output

```bash
python -m pytest -v
```

---

## Run one test file

Example:

```bash
python -m pytest tests/test_login.py
```

---

## Run one specific test

Example:

```bash
python -m pytest tests/test_login.py::TestLogin::test_TC_201_login_with_valid_credentials
```

---

# Allure Reports

## What Allure is used for

Allure creates a visual test report showing:

- passed tests
- failed tests
- skipped tests
- test duration
- error messages
- stack traces
- screenshots for failed tests
- test grouping by epic, feature and story

---

## Generate Allure results

Run:

```bash
python -m pytest --alluredir=allure-results
```

This creates raw Allure result files in:

```text
allure-results/
```

---

## Open the Allure report

Run:

```bash
allure serve allure-results
```

This command:

1. Generates the HTML report
2. Starts a local web server
3. Opens the report in the browser

---

## Clean and regenerate report

Linux / macOS:

```bash
rm -rf allure-results allure-report screenshots
python -m pytest --alluredir=allure-results
allure serve allure-results
```

Windows Command Prompt:

```cmd
rmdir /s /q allure-results
rmdir /s /q allure-report
rmdir /s /q screenshots
python -m pytest --alluredir=allure-results
allure serve allure-results
```

If a folder does not exist yet, Windows may show a message. That is normal.

---

## Screenshots in Allure

Screenshots are attached to the Allure report only when a test fails.

The screenshot logic is implemented in:

```text
tests/conftest.py
```

When a test fails, the framework:

1. Saves a screenshot in the `screenshots/` folder
2. Attaches the screenshot to the failed test in the Allure report

To confirm screenshot attachment works, temporarily add a failing test:

```python
def test_debug_screenshot(driver):
    driver.get("https://www.demoblaze.com/index.html")
    assert False
```

Then run:

```bash
python -m pytest --alluredir=allure-results
allure serve allure-results
```

Open the failed test in Allure and check the Attachments section.

Remove the debug test after verification.

---

# Running from PyCharm

## Run tests in PyCharm

1. Open the project in PyCharm
2. Select the correct Python interpreter:
   - `.venv/bin/python` on Linux/macOS
   - `.venv\Scripts\python.exe` on Windows
3. Open Run > Edit Configurations
4. Create a Pytest configuration
5. Set target to `tests`
6. Add this to additional arguments:

```text
--alluredir=allure-results
```

7. Run the configuration

---

## Open Allure report from PyCharm terminal

After tests finish, open the PyCharm terminal and run:

```bash
allure serve allure-results
```

If Allure works in an external terminal but not in PyCharm, then PyCharm does not have the same PATH environment variable.

In that case, run this in the external terminal:

```bash
which allure
```

Then use the full path inside PyCharm.

Example:

```bash
/usr/local/bin/allure serve allure-results
```

---

# Common Problems and Fixes

## `ModuleNotFoundError: No module named 'config'`

Make sure these files exist:

```text
config/__init__.py
pages/__init__.py
tests/__init__.py
```

Also run tests from the project root.

Correct:

```bash
python -m pytest
```

Incorrect:

```bash
cd tests
python -m pytest
```

---

## `ModuleNotFoundError: No module named 'selenium'`

This means dependencies are not installed in the active virtual environment.

Fix:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows:

```cmd
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

---

## `ModuleNotFoundError: No module named 'allure'`

This means the Python Allure plugin is missing from the active virtual environment.

Fix:

```bash
python -m pip install allure-pytest
```

---

## `allure: command not found`

This means the Allure CLI is not installed or not available in PATH.

Install Allure CLI:

```bash
npm install -g allure-commandline --save-dev
```

Then verify:

```bash
allure --version
```

If it works outside PyCharm but not inside PyCharm, use the full path to the `allure` command.

---

## `SessionNotCreatedException: Chrome instance exited`

This usually means Chrome could not start.

Typical fixes are already included in `conftest.py`:

```python
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
```

Also verify that Chrome or Chromium is installed.

---

# Test Approach

The tests are based on real user journeys.

Examples:

```text
Open Homepage -> Select Category -> Select Product -> Add to Cart
-> Open Cart -> Place Order -> Fill Form -> Confirm Purchase
```

The framework validates:

- UI element visibility
- Alert messages
- Product data
- Cart contents
- Price consistency
- Purchase confirmation

---

# Notes and Limitations

- The tests run against a public demo site
- The database cannot be reset
- Some registration tests may depend on existing application data
- UI tests can be slower and more fragile than API or unit tests
- The site behavior may change because it is not controlled by this project

---

# Future Improvements

Possible future improvements:

- Add CI/CD pipeline with GitHub Actions
- Add cross-browser support
- Add parallel execution with `pytest-xdist`
- Add environment-specific configuration
- Add test data files for larger DDT coverage
- Add retry logic for known flaky UI behavior
