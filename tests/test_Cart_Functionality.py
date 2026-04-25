import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




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
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep (5)

        # verifying that we see the previously selected monitor
        monitor_name = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid h2")

        # extracting the monitor name
        actual_result = monitor_name[0].text
        expected_result = "Apple monitor 24"

        # comparing to expected name
        self.assertEqual(actual_result, expected_result)

        # verifying that ADD TO CART button is visible
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button_text = add_to_card_button.text
        add_to_card_button_expected = "Add to cart"

        # Assertion
        self.assertEqual(add_to_card_button_expected, add_to_card_button.text)

    def test_TC_502_Add_Product_To_Cart_Popup_Confirmation(self):

        # step 1 of the TC_502
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep(5)

        #  step 2 of the TC_502
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep(5)

        # step 3 of the TC_502
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button.click()
        sleep(5)

# expected result of the TC_502
        expected_message = 'Product added'

        # wait for Pop up to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # get Pop up text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

    def test_TC_503_View_Cart_With_One_Added_Product(self):

        # step 1 of the TC_503
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep(2)

        #  step 2 of the TC_503
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep(2)

        # step 3 of the TC_503
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button.click()
        sleep(2)

        # define element that contains the pop-up
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # step 4 of the TC_503 (clicks OK)
        alert.accept()
        sleep(2)

        # step 5 of the TC_503
        menu_cart_link = self.driver.find_element(By.ID, "cartur")
        menu_cart_link.click()

        sleep(2)

        # deifinig prducts added to the cart page
        products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr") #number of rows in the table

        # checking if PLACE ORDER button is visible
        place_order_btn = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")


        # Assertions
        self.assertEqual(len(products), 1)
        assert place_order_btn.is_displayed()

     # close browser after each test case
    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()





