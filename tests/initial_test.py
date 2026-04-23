import unittest
from selenium import webdriver

# creating test setup
class TestPageTitle(unittest.TestCase):
    def setUp(self):

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