from Day12 import OpenChrome as oc
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys

oc.driver.get("https://www.wikipedia.org/")

dd=oc.driver.find_element_by_xpath("//select[@name='language']")

sel = Select(dd)

sel.select_by_visible_text("Slovenščina")

time.sleep(5)

sel.select_by_index("15")

time.sleep(5)

sel.select_by_value("tr")

time.sleep(5)

oc.driver.find_element_by_xpath("//input[@id='searchInput']").send_keys("हिन्दी",Keys.ENTER)

time.sleep(5)
oc.driver.quit()