from Day12 import OpenChrome as oc
import time

oc.driver.get("https://www.redbus.in/")

oc.driver.maximize_window()

oc.driver.find_element_by_id("src").send_keys("Bang")

time.sleep(4)
pickupPoints = oc.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")

time.sleep(4)

print(len(pickupPoints))

time.sleep(4)

for v in pickupPoints:
    if v.text=="Majestic, Bangalore":
        v.click()
        break
time.sleep(4)
#print(v.text)
time.sleep(4)
oc.driver.quit()