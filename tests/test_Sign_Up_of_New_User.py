from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
##from data_tools import *
from time import sleep
import unittest

class Test_Sign_Up_Of_New_User(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

# trying to sign up a user without entering a username and password
    def test_TC_105_Sign_Up_With_Empty_Username_And_Password(self):
        #  step 1 of the TC_105
        element = self.driver.find_element(By.XPATH, '//*[@id="signin2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_105
        username_input = self.driver.find_element(By.ID, "sign-username")
        username_input.send_keys("")
        # step 3 of the TC_105
        password_input = self.driver.find_element(By.ID, "sign-password")
        password_input.send_keys("")
        # step 4 of the TC_105
        button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        # expected result of the TC_105
        expected_message = 'Please fill out Username and Password.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# trying to sign up a user without entering a password
    def test_TC_106_Sign_Up_With_Missing_Password(self):
        #  step 1 of the TC_106
        element = self.driver.find_element(By.XPATH, '//*[@id="signin2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_106
        username_input = self.driver.find_element(By.ID, "sign-username")
        username_input.send_keys("Andrzej")
        # step 3 of the TC_106
        password_input = self.driver.find_element(By.ID, "sign-password")
        password_input.send_keys("")
        # step 4 of the TC_106
        button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        # expected result of the TC_106
        expected_message = 'Please fill out Username and Password.'
        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

# trying to sign up a user without entering a Username
    def test_TC_107_Sign_Up_With_Missing_Username(self):
        #  step 1 of the TC_107
        element = self.driver.find_element(By.XPATH, '//*[@id="signin2"]').click()
        sleep(5)
        # Data visible in the form:
        # step 2 of the TC_107
        username_input = self.driver.find_element(By.ID, "sign-username")
        username_input.send_keys("")
        # step 3 of the TC_107
        password_input = self.driver.find_element(By.ID, "sign-password")
        password_input.send_keys("123456")
        # step 4 of the TC_107
        button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        # expected result of the TC_107
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

