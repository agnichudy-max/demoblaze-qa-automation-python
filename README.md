# Demoblaze Automated Tests (Python + Selenium)

## Project Overview

This project contains **automated UI tests** for the Demoblaze e-commerce application using:

* **Python**
* **Selenium WebDriver**
* **unittest (primary framework)**
* **pytest (optional runner)**

The project demonstrates a **Page Object Model (POM)** design for maintainable and scalable test automation.

---

## Key Features

* End-to-end UI test automation
* Page Object Model architecture
* Positive and negative test scenarios
* Dynamic test data using **Faker**
* Compatible with **unittest**

---

## Scope of Testing

The automated tests cover:

* User Registration (Sign Up)
* User Login (valid & invalid scenarios)
* Product Categories Navigation
* Product Details Page
* Cart Functionality
* Purchase / Payment Flow

---

## Tech Stack

* **Language:** Python
* **Test Framework:** unittest
* **Automation Tool:** Selenium WebDriver
* **Browser:** Google Chrome
* **Test Data:** Faker
* **Environment:** Cross-platform (Windows / Linux / macOS)

---

## Project Structure

```id="9c1q9v"
demoblaze-selenium-python-tests/
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_details_page.py
│   ├── cart_page.py
│   ├── login_modal.py
│   ├── signup_modal.py
│   ├── order_modal.py
│
├── tests/
│   ├── initial_test.py
│   ├── test_Log_In_Of_Active_User.py
│   ├── test_Sign_Up_of_New_User.py
│   ├── test_Displaying_Category_Functionality.py
│   ├── test_Cart_Functionality.py
│   ├── test_Payment_Functionality.py
│
├── requirements.txt
└── README.md
```

---

## Test Architecture

This project follows the **Page Object Model (POM)**:

* Each page/modal is represented as a class in `/pages`
* Tests interact with page objects instead of raw Selenium code
* Improves readability and maintainability

---

## How to Run Tests

### 1. Clone the repository

```id="b8o2m4"
git clone https://github.com/agnichudy-max/demoblaze-qa-automation-python.git
cd demoblaze-qa-automation-python
```

---

### 2. Install dependencies

```id="t4zv2y"
pip install -r requirements.txt
```

---

## Running Tests

### Option 1: Run with unittest (default)

```id="s7n6ax"
python -m unittest discover -s tests
```

---

## Test Approach

* Functional testing based on real user journeys
* Combination of:

  * Positive tests (valid flows)
  * Negative tests (error handling & validation)

Validation includes:

* UI element visibility
* Alerts and popups
* Data consistency (e.g., cart vs order total)

---

## Example Test Flow

```id="0s5kqm"
Open Homepage → Select Category → Select Product → Add to Cart
→ Open Cart → Place Order → Fill Form → Confirm Purchase
```

---

## Notes & Limitations

* Tests run against a public demo site (data may change)
* No backend/database access → UI validation only
* Some tests rely on application state (e.g., cart content)

---

## Future Improvements

* Add pytest fixtures (driver setup instead of setUp)
* Integrate CI/CD (GitHub Actions)
* Add logging and screenshots on failure
* Parallel execution (pytest-xdist)
* Headless browser execution

---
