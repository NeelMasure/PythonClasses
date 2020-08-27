from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.flipkart.com")
oc.driver.maximize_window()

oc.driver.find_element_by_xpath("//button[text()='✕']").click()

oc.driver.find_element_by_xpath("//span[contains(text(), 'Cart')]").click()

time.sleep(2)

oc.driver.back()

oc.driver.find_element_by_xpath("//span[(text()= 'Cart')]").click()

time.sleep(5)
oc.driver.quit()
