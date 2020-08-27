from Day12 import OpenChrome as oc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import time

oc.driver.maximize_window()

oc.driver.get("https://www.facebook.com/")

oc.driver.find_element_by_xpath("//a[@id='u_0_2']").click()

oc.driver.find_element_by_name("firstname").send_keys("Neel",Keys.ENTER)

oc.driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Masure")

oc.driver.find_element_by_name("reg_email__").send_keys("masureneel96@gmail.com")

D= oc.driver.find_element_by_xpath("//select[@id='day']")

sel= Select(D)

sel.select_by_value("6")

oc.driver.find_element_by_xpath("//select[@id='month']")

sel.select_by_value("5")

oc.driver.find_element_by_xpath("//select[@id='year']")

sel.select_by_value("1996")

oc.driver.find_element_by_xpath("//input[@id='u_b_3']").click()

time.sleep(5)

oc.driver.quit()







