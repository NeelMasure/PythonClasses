from Day12 import OpenChrome as oc
import time


oc.driver.get("https://www.amazon.in/")
oc.driver.maximize_window()

backtoTop= oc.driver.find_element_by_xpath("//span[text()='Back to top']")

oc.driver.execute_script("arguments[0].scrollIntoView();",backtoTop)

time.sleep(4)
oc.driver.quit()