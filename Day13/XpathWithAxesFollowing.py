from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys
import time

oc.driver.get("https://the-internet.herokuapp.com/tables")
oc.driver.maximize_window()
name = "Smith"
val = oc.driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[contains(text(),'"+name+"')]//following::td[3]").text


print(val)

time.sleep(3)
oc.driver.quit()
