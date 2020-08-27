from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys

oc.driver.get("https://www.amazon.com")

oc.driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone",Keys.ENTER)
