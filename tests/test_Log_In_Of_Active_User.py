from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
##from data_tools import *
from time import sleep
import unittest

# creating test setup
class Test_Log_In_of_Active_User(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

# trying to log in a user with entering valid username and password
    def test_TC_201_Log_In_With_Valid_Credentials(self):
        #  step 1 of the TC_201
        element = self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_201
        username_input = self.driver.find_element(By.ID, "loginusername")
        username_input.send_keys("aga-chudy")
        # step 3 of the TC_201
        password_input = self.driver.find_element(By.ID, "loginpassword")
        password_input.send_keys("suntago")
        # step 4 of the TC_201
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='logInModal']//button[normalize-space()='Log in']")))
        login_button.click()
        sleep(5)
        # expected result of the TC_201
        expected_welcome_message = 'Welcome aga-chudy'
        actual_welcome_message = self.driver.find_element(By.ID,'nameofuser').text
        # comparing actual result with expected result of TC_201
        self.assertEqual(expected_welcome_message, actual_welcome_message)

# trying to log in with non-existing user
    def test_TC_202_Log_In_With_Non_Existing_User(self):
        #  step 1 of the TC_202
        element = self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_202
        username_input = self.driver.find_element(By.ID, "loginusername")
        username_input.send_keys("...,,,!!!")
        # step 3 of the TC_202
        password_input = self.driver.find_element(By.ID, "loginpassword")
        password_input.send_keys("suntago")
        # step 4 of the TC_202
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='logInModal']//button[normalize-space()='Log in']")))
        login_button.click()
        sleep(5)
        # expected result of the TC_202
        expected_message = 'User does not exist.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# trying to log in with invalid password
    def test_TC_203_Log_In_With_Invalid_Password(self):
        #  step 1 of the TC_203
        element = self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_203
        username_input = self.driver.find_element(By.ID, "loginusername")
        username_input.send_keys("aga-chudy")
        # step 3 of the TC_203
        password_input = self.driver.find_element(By.ID, "loginpassword")
        password_input.send_keys("...,,,!!!")
        # step 4 of the TC_203
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='logInModal']//button[normalize-space()='Log in']")))
        login_button.click()
        sleep(5)
        # expected result of the TC_203
        expected_message = 'Wrong password.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# trying to log in with missing password
    def test_TC_204_Log_In_With_Missing_Password(self):
        #  step 1 of the TC_204
        element = self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_204
        username_input = self.driver.find_element(By.ID, "loginusername")
        username_input.send_keys("aga-chudy")
        # step 3 of the TC_204
        password_input = self.driver.find_element(By.ID, "loginpassword")
        password_input.send_keys("")
        # step 4 of the TC_204
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='logInModal']//button[normalize-space()='Log in']")))
        login_button.click()
        sleep(5)
        # expected result of the TC_204
        expected_message = 'Please fill out Username and Password.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# trying to log in with invalid password format
    def test_TC_204_Log_In_With_Missing_Password(self):
        #  step 1 of the TC_204
        element = self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_204
        username_input = self.driver.find_element(By.ID, "loginusername")
        username_input.send_keys("aga-chudy")
        # step 3 of the TC_204
        password_input = self.driver.find_element(By.ID, "loginpassword")
        password_input.send_keys("")
        # step 4 of the TC_204
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='logInModal']//button[normalize-space()='Log in']")))
        login_button.click()
        sleep(5)
        # expected result of the TC_204
        expected_message = 'Please fill out Username and Password.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# close browser after each test case
def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
    unittest.main()