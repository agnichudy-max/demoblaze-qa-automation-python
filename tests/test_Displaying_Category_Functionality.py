from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
##from data_tools import *
from time import sleep
import unittest

# creating test setup
class Test_Displaying_Category_Functionality(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

# checking if MONITORS button opens monitors category
    def test_TC_401_View_Monitors_Category_With_Pagination_Buttons(self):
        #  step 1 of the TC_401
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        # expected result of the TC_401
        expected_previous_button = 'Previous'
        actual_previous_button = self.driver.find_element(By.ID, 'prev2').text
        # comparing actual result with expected result of TC_401
        self.assertEqual(expected_previous_button, actual_previous_button)
        expected_next_button = 'Next'
        actual_next_button = self.driver.find_element(By.ID, 'next2').text
        self.assertEqual(expected_next_button, actual_next_button)

    # checking if NEXT button opens next page with more products from the same category
    def test_TC_402_Navigate_To_Next_Page_In_Monitors_Category(self):
            #  step 1 of the TC_402
            monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
            monitor_link.click()
            # expected result of the TC_402
            expected_previous_button = 'Previous'
            actual_previous_button = self.driver.find_element(By.ID, 'prev2').text
            # comparing actual result with expected result of TC_401
            self.assertEqual(expected_previous_button, actual_previous_button)
            expected_next_button = 'Next'
            actual_next_button = self.driver.find_element(By.ID, 'next2').text
            self.assertEqual(expected_next_button, actual_next_button)
            # step 2 of the TC_402: click the NEXT button
