# Demoblaze Automated Tests (Python + Selenium)

##  Project Overview

This project contains **automated test scenarios and test cases** for the Demoblaze e-commerce web application.
The tests are implemented using **Python** and **Selenium WebDriver** to validate core functionalities of the application.

The goal of this project is to demonstrate practical skills in:

* Test case design
* Automated UI testing
* Quality assurance processes

---

##  Scope of Testing

The automated tests cover the following functionalities:

*  User Registration (Sign Up)
*  User Login / Logout
*  Product Categories Navigation
*  Cart Functionality
*  Purchase / Payment Process

---

##  Tech Stack

* **Language:** Python
* **Framework/Tool:** Selenium WebDriver
* **Browser:** Google Chrome
* **Environment:** Ubuntu / Cross-platform

---

##  Project Structure

```
demoblaze-selenium-python-tests/
│
├── tests/
│   ├── initial_test.py
│   ├── test_Log_In_Of_Active_User.py
│   ├── test_Displaying_Category_Functionality.py
│   ├── test_Sign_Up_of_New_User.py
│   ├── test_Cart_Functionality.py

├── requirements.txt
└── README.md
```

---

##  How to Run Tests

### 1. Clone the repository

```
git clone https://github.com/agnichudy-max/demoblaze-qa-automation-python.git
cd demoblaze-qa-automation-python
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run tests
Observe the path where pytest is installed in your system.
```
<path>pytest
```

---

##  Test Approach

* Functional testing based on real user scenarios
* Focus on **negative test cases** due to limited backend/database access
* Validation of:

  * Input fields
  * Pop-up messages
