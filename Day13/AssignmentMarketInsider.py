from Day12 import OpenChrome as oc
import time

oc.driver.get("https://markets.businessinsider.com/stocks")
oc.driver.maximize_window()
name = "Smith"
val = oc.driver.find_element_by_xpath().text

print(val)

time.sleep(3)
oc.driver.quit()