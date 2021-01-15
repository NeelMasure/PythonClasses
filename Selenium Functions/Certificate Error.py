from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


ops= ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--incognito")
ops.add_argument("--ignore-certificate-errors")
drive = Chrome(ChromeDriverManager().install(),options=ops)



drive.get("https://cacert.org/")

"""
SSL - Secure Socket Layer
https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

"""




