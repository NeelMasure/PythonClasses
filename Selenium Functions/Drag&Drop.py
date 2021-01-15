from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

oc.driver.maximize_window()

oc.driver.get("http://demo.guru99.com/test/drag_drop.html")

src= oc.driver.find_element_by_xpath("//*[@id='fourth']/a[1]")
dec= oc.driver.find_element_by_xpath("//*[@id='amt7']/li")

act= ActionChains(oc.driver)
act.drag_and_drop(src,dec).perform()
