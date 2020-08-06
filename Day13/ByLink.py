from Day12 import OpenChrome as op
from selenium.webdriver.common.keys import Keys
import time

"""op.driver.get("https://www.google.com")
op.driver.maximize_window()
op.driver.find_element_by_link_text("मराठी").click()
time.sleep(5)
op.driver.quit()"""

op.driver.get("https://www.google.com")
op.driver.maximize_window()
op.driver.find_element_by_partial_link_text("Ima").click()
time.sleep(5)
op.driver.quit()