from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
ops = ChromeOptions()
# https://chromedriver.chromium.org/capabilities
# https://stackoverflow.com/questions/38335671/where-can-i-find-a-list-of-all-available-chromeoption-arguments

ops.add_argument("--disable-notifications")
driver= Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.icicibank.com/")
driver.maximize_window()
driver.find_element_by_class_name("product-personal-login-new").click()