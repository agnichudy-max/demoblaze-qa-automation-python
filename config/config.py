# URL of the website to be tested
BASE_URL = "https://www.demoblaze.com/index.html"

# Maximum wait time in seconds
# Selenium will wait up to 10 seconds for elements to appear
# before throwing an error
TIMEOUT = 10

# Determines whether the browser should run in headless mode
# False = browser window is visible
# True  = browser runs in background without UI
HEADLESS = True

# Folder where screenshots will be stored
# ": str" it means this variable should contain a string
SCREENSHOT_DIR: str = "screenshots"