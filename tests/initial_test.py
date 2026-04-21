from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
##from data_tools import *
from time import sleep
import unittest

#
class TestPageTitle(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

# checking that the homepage title is STORE
    def test_title(self):
        actual_title = self.driver.title
        expected_title = 'STORE'
        self.assertEqual(actual_title, expected_title)

# close browser after each test case
def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
    unittest.main()