from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
ops= ChromeOptions()
ops.add_argument("--disable-notifications")
drive = Chrome(ChromeDriverManager().install(),options=ops)



drive.get("https://www.icicibank.com/")
drive.find_element_by_id("login-btn").click()



