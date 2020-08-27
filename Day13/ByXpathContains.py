from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.amazon.in")
oc.driver.maximize_window()

oc.driver.find_element_by_xpath("//a[contains(text(),'Deals')]").click()

time.sleep(5)

oc.driver.find_element_by_xpath("//a[text()='Gift Cards']").click()
oc.driver.quit()
