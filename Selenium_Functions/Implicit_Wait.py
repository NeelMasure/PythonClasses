from Day12 import OpenChrome as oc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

oc.driver.maximize_window()

oc.driver.get("https://www.google.com")
oc.driver.implicitly_wait(30)

links= oc.driver.find_elements_by_tag_name("a")
print("Total no of links",len(links))

for l in links:
    print(l.text +"---->"+l.get_attribute("href"))

time.sleep(4)
oc.driver.quit()
