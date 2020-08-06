from Day12 import OpenChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.amazon.com")
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone", Keys.ENTER)
time.sleep(5)
op.driver.quit()