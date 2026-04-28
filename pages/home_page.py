from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# HomePage represents the main landing page of the application.
# It inherits from BasePage, so it already has access to:
# - self.driver (browser control)
# - self.wait (explicit wait handling)
class HomePage(BasePage):

    # ===== LOCATORS =====
    # These are reusable selectors for elements on the page.

    # Navigation links
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    CART_LINK = (By.ID, "cartur")

    # Product-related elements
    # Selects all product title links (e.g., product cards)
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".card-title a")

    # Pagination buttons
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(),'Previous')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")

    # Locator for the welcome message shown after successful login
    # Example HTML: <a id="nameofuser">Welcome username</a>
    WELCOME_MESSAGE = (By.ID, "nameofuser")

    # ===== ACTION METHODS =====

    def get_welcome_message(self):
        # Wait until the welcome message element becomes visible on the page
        # This is important because the UI updates after login are asynchronous
        element = self.wait.until(
            EC.visibility_of_element_located(self.WELCOME_MESSAGE)
        )

        # Return the text content of the element
        # Example return value: "Welcome aga-chudy"
        return element.text

    def open_login_modal(self):
        # Waits until the login link is clickable, then clicks it.
        # This typically opens a login popup/modal.
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    def open_signup_modal(self):
        # Same pattern as login, but for the signup modal.
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_LINK)).click()

    def open_cart(self):
        # Navigates to the cart page by clicking the cart link.
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()

    def select_category(self, category_name):
        # Clicks a category by its visible text (e.g., "Phones", "Laptops").
        # By.LINK_TEXT finds <a> elements with matching text.
        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, category_name))
        ).click()

    def select_product(self, product_name):
        # Clicks a product by its name (visible link text).
        # This usually navigates to the product details page.
        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, product_name))
        ).click()

    # ===== DATA / QUERY METHODS =====

    def get_visible_product_names(self):
        # Waits until product titles are visible on the page.
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_TITLES)
        )

        # Extracts and returns clean text for each product.
        # .strip() removes extra whitespace (good practice).
        return [product.text.strip() for product in products]

    def is_previous_button_visible(self):
        # find_elements returns a list (empty if nothing found),
        # so it avoids raising an exception.
        buttons = self.driver.find_elements(*self.PREVIOUS_BUTTON)

        # Returns True only if:
        # - at least one button exists
        # - and it is visible on the page
        return bool(buttons and buttons[0].is_displayed())

    def is_next_button_visible(self):
        # Same logic as above, but for the "Next" button.
        buttons = self.driver.find_elements(*self.NEXT_BUTTON)
        return bool(buttons and buttons[0].is_displayed())