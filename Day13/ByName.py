from Day12 import OpenChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.google.com")
op.driver.maximize_window()
op.driver.find_element_by_name("q").send_keys("Manual Testing",Keys.ENTER)
time.sleep(5)
op.driver.quit()