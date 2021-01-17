from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

oc.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

oc.driver.maximize_window()

rtButton = oc.driver.find_element_by_xpath("//span[text()='right click me']")
time.sleep(4)
act=ActionChains(oc.driver)
time.sleep(4)
act.context_click(rtButton).perform()

time.sleep(4)
oc.driver.quit()