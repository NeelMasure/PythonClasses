from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
oc.driver.maximize_window()

oc.driver.get("https://www.redbus.in/")
time.sleep(4)

oc.driver.find_element_by_css_selector("#src").send_keys("Bang")
time.sleep(4)
src=oc.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
print(len(src))
for s in src:
    if s.text =="Marathahalli, Bangalore":
        s.click()
        break

time.sleep(4)
oc.driver.find_element_by_css_selector("#dest").send_keys("Pun")
time.sleep(4)
src=oc.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
print(len(src))
for s in src:
    if s.text =="Wakad, Pune":
        s.click()
        break

time.sleep(4)

oc.driver.find_element_by_css_selector(".fl.icon-calendar_icon-new.icon-onward-calendar.icon").click()
time.sleep(4)

month=oc.driver.find_elements_by_xpath("//table[@class='rb-monthTable first last']/tbody/tr/td")
for m in month:
    if m!="Jan 2021":
        oc.driver.find_element_by_xpath("//button[text()='>']").click()
        break

time.sleep(4)

day=oc.driver.find_elements_by_xpath("//table[@class='rb-monthTable first last']/tbody/tr/td")
for d in day:
    if d.text=="14":
        d.click()
        break

time.sleep(4)

oc.driver.find_element_by_xpath("//button[text()='Search Buses']").click()
time.sleep(4)
oc.driver.quit()