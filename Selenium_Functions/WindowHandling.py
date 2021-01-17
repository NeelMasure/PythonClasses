from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Selenium_Functions import Generic as gen

oc.driver.maximize_window()

oc.driver.get("https://www.canarabank.com/")

login=oc.driver.find_element_by_xpath("//p[text()='LOGIN']")
time.sleep(4)
gen.mouseHover(oc.driver,login)

win1=oc.driver.current_window_handle
print("Parent Window ID",win1)
print("Page Title:"+ oc.driver.title)
time.sleep(4)

netBank=oc.driver.find_element_by_xpath("//a[text()='Net Banking - Canara']")
time.sleep(4)
gen.actionClick(oc.driver,netBank)

listofwin=oc.driver.window_handles

for wins in listofwin:
    print(wins)

time.sleep(4)
oc.driver.switch_to_window(listofwin[1])
print("Page Title:"+ oc.driver.title)
oc.driver.close()

oc.driver.switch_to_window(listofwin[0])
print("Page Title:"+ oc.driver.title)
time.sleep(4)
oc.driver.quit()

