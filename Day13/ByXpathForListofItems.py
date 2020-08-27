from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.flipkart.com")
oc.driver.maximize_window()

oc.driver.find_element_by_xpath("//button[text()='✕']").click()

oc.driver.find_element_by_class_name("LM6RPg").send_keys("Iphone XR 11", Keys.ENTER)

oc.driver.find_element_by_xpath("//*[text()='Apple iPhone XR (Yellow, 128 GB)']").click()

time.sleep(3)
oc.driver.quit()
