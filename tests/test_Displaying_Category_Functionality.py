import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Displaying_Category_Functionality(unittest.TestCase):
    def setUp(self):

        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

# checking if MONITORS button opens monitors category
    def test_TC_401_Open_Monitors_Category_Page(self):

        #  step 1 of the TC_401
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()

        # Waiting for items to load
        time.sleep(2)

        # Get all product titles
        products = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")

        # Extract text
        product_names = [p.text.strip() for p in products]

        # Expected products
        expected = ["Apple monitor 24", "ASUS Full HD"]

        # Assertions
        assert len(product_names) == 2, f"Expected 2 monitors, got {len(product_names)}"
        assert set(product_names) == set(expected), f"Unexpected products: {product_names}"

    # checking if Pagination (NEXT PREVIOUS) are not visible
    def test_TC_402_Verify_Pagination_Buttons_Not_Visible_For_Small_Product_List(self):

            #  step 1 of the TC_402
            monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
            monitor_link.click()

            # Try to locate Previous button
            previous_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Previous')]")

            # Try to locate Next button
            next_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Next')]")

            # If buttons exist, verify they are not visible
            if previous_buttons:
                assert not previous_buttons[0].is_displayed(), "Previous button is visible, but it should not be."
            if next_buttons:
                assert not next_buttons[0].is_displayed(), "Next button is visible, but it should not be."

    # close browser after each test case
    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()