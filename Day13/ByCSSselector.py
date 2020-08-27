from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.amazon.in")
oc.driver.maximize_window()
oc.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Iphone XR",Keys.ENTER)
time.sleep(2)
oc.driver.quit()