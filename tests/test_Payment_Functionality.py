import unittest
from time import sleep
from re import search
import wait
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# creating test setup
class Test_Payment_functionality(unittest.TestCase):
    def setUp(self):
        # 1. Open the home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.demoblaze.com/index.html')
        self.driver.implicitly_wait(15)

    def test_TC_601_Open_Order_Form_From_Cart(self):
        # precondition from TC_503
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep(2)

        # precondition from TC_503
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep(2)

        # precondition from TC_503
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button.click()
        sleep(2)

        # precondition from TC_503
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # precondition from TC_503
        alert.accept()
        sleep(2)

        # precondition from TC_503
        menu_cart_link = self.driver.find_element(By.ID, "cartur")
        menu_cart_link.click()

        sleep(2)

        # deifinig prducts added to the cart page
        products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")  # number of rows in the table

        # finding PLACE ORDER button
        place_order_btn = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")

        # step 1 of TC_601
        place_order_btn.click()
        sleep(2)

        # checking if ORDER_FORM is visible
        order_form = self.driver.find_element(By.XPATH, '//*[@id="orderModal"]')

        # Assertions
        assert order_form.is_displayed()

    def test_TC_602_Validate_Empty_Purchase_Form_Error_Message(self):

        # precondition from TC_503
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep(2)

        # precondition from TC_503
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep(2)

        # precondition from TC_503
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button.click()
        sleep(2)

        # precondition from TC_503
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # precondition from TC_503
        alert.accept()
        sleep(2)

        # precondition from TC_503
        menu_cart_link = self.driver.find_element(By.ID, "cartur")
        menu_cart_link.click()

        sleep(2)

        # deifinig prducts added to the cart page
        products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")  # number of rows in the table

        # finding PLACE ORDER button
        place_order_btn = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")

        # step 1 of TC_602
        place_order_btn.click()
        sleep(2)

        # step 4 of TC_602
        # finding PURCHASE button
        purchase_btn = self.driver.find_element(By.XPATH, "//button[text()='Purchase']")

        # click PURCHASE button
        purchase_btn.click()
        sleep(2)

        # expected result of the TC_602
        expected_message = 'Please fill out Name and Creditcard.'

        # wait for alert to appear
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # get alert text
        alert_text = alert.text
        self.assertEqual(alert_text, expected_message)

    def test_TC_603_Complete_Purchase_With_Name_And_Card(self):
        # precondition from TC_503
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()
        sleep(2)

        # precondition from TC_503
        apple_monitor_link = self.driver.find_element(By.LINK_TEXT, "Apple monitor 24")
        apple_monitor_link.click()
        sleep(2)

        # precondition from TC_503
        add_to_card_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_card_button.click()
        sleep(2)

        # precondition from TC_503
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # precondition from TC_503
        alert.accept()
        sleep(2)

        # precondition from TC_503
        menu_cart_link = self.driver.find_element(By.ID, "cartur")
        menu_cart_link.click()

        sleep(2)

        # extract total price from the cart page
        cart_total_price = self.driver.find_element(By.ID, "totalp").text
        expected_cart_total_price = '400'

        # asserting that expected value equals the actual value
        self.assertEqual(cart_total_price, expected_cart_total_price)

        # deifinig prducts added to the cart page
        products = self.driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")  # number of rows in the table

        # finding PLACE ORDER button
        place_order_btn = self.driver.find_element(By.XPATH, "//button[text()='Place Order']")

        # step 1 of TC_602
        place_order_btn.click()
        sleep(2)

        # extracting total price from purchase modal window
        purchase_modal_window_price = self.driver.find_element(By.ID, "totalm").text
        expected_purchase_modal_window_price = "Total: " + str(int(cart_total_price))

        # asserting that price is modal window equals cart total price
        self.assertEqual(purchase_modal_window_price, expected_purchase_modal_window_price)

        # step 2 of TC_603
        name_input = self.driver.find_element(By.ID, "name")
        name_input.send_keys("aga-chudy")

        # step 3 of TC_603
        credit_card_input = self.driver.find_element(By.ID, "card")
        credit_card_input.send_keys("123456")

        # finding PURCHASE button
        purchase_btn = self.driver.find_element(By.XPATH, "//button[text()='Purchase']")

        # step 4 of TC_603 click PURCHASE button
        purchase_btn.click()
        sleep(5)

        # finding purchase confirmation window
        success_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible"))
        )
        # extracting text from popup
        popup_text = success_popup.text

        # validating that paid price from confirmation window equals total price from cart page
        assert "Amount: 400 USD" in popup_text








