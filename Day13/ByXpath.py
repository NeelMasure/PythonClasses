from Day12 import OpenChrome as oc
from selenium.webdriver.common.keys import Keys

oc.driver.get("https://www.google.in/")
oc.driver.maximize_window()

# Absolute xpath

# oc.driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div/div/div/div[2]/input").send_keys("Appium Jobs",Keys.ENTER)

oc.driver.find_element_by_xpath("//input[@name='q' and @class='gLFyf gsfi' and @title 'Search']").send_keys("facebook",Keys.ENTER)
