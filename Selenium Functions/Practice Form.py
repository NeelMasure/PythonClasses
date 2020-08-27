from Day12 import OpenChrome as oc
from selenium.webdriver.support.select import Select
oc.driver.get("https://demoqa.com/automation-practice-form/")

oc.driver.find_element_by_id("firstName").send_keys("Neel")

oc.driver.find_element_by_id("lastName").send_keys("Masure")

oc.driver.find_element_by_id("userEmail").send_keys("masureneel@gmail.com")

oc.driver.find_element_by_class_name("custom-control-label").click()

oc.driver.find_element_by_id("userNumber").send_keys("8378975558")

oc.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--006 react-datepicker__day--selected']").click()

oc.driver.quit()