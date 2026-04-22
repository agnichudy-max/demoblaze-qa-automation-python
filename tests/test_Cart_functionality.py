from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
##from data_tools import *
from time import sleep
import unittest

# creating test setup
class Test_Cart_functionality(unittest.TestCase):
    def setUp(self):
        # Preconditions
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

    def test_TC_501_View_Product_Details_Page_Load(self):
        #  step 1 of the TC_501
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep (5)
        #  step 2 of the TC_501
        product = product.self self.driver.find_element(By.ID, "loginusername")
