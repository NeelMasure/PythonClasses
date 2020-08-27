from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://www.amazon.in")
oc.driver.maximize_window()

oc.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Iphone",Keys.ENTER)

time.sleep(2)

oc.driver.get("https://www.facebook.com")
oc.driver.find_element_by_xpath("//input[@type='text']").send_keys("Neel Masure")