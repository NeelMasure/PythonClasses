from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

oc.driver.maximize_window()

oc.driver.get("https://www.myntra.com//")

women= oc.driver.find_element_by_xpath("//a[text()='Women'][1]")
act = ActionChains(oc.driver)

act.move_to_element(women).perform()
time.sleep(4)
saree= oc.driver.find_elements_by_xpath("//a[text()='Sarees'][1]")
# act.click(saree).perform()
act1=ActionChains(oc.driver)
act1.move_to_element(saree).perform()
time.sleep(4)

oc.driver.quit()