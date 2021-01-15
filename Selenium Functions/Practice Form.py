from Day12 import OpenChrome as oc
from selenium.webdriver.support.select import Select
import time

oc.driver.maximize_window()

oc.driver.get("https://demoqa.com/automation-practice-form/")

time.sleep(3)

oc.driver.find_element_by_id("firstName").send_keys("Neel")
time.sleep(3)

oc.driver.find_element_by_id("lastName").send_keys("Masure")
time.sleep(3)

oc.driver.find_element_by_id("userEmail").send_keys("masureneel@gmail.com")
time.sleep(3)

oc.driver.find_element_by_class_name("custom-control-label").click()
time.sleep(3)

oc.driver.find_element_by_id("userNumber").send_keys("8378975558")
time.sleep(3)

time.sleep(3)

oc.driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").click()

month = oc.driver.find_element_by_xpath("//select[@class='react-datepicker__month-select']")
year =  oc.driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']")

sel=Select(month)

sel.select_by_value("4")

sel=Select(year)

sel.select_by_value("1996")

oc.driver.find_element_by_xpath("//div[text()='6']").click()

time.sleep(3)



oc.driver.find_element_by_xpath("//label[text()='Sports']").click()

time.sleep(3)

oc.driver.find_element_by_xpath("//label[text()='Music']").click()

oc.driver.find_element_by_xpath("//input[@id='uploadPicture']").send_keys("C:/Users/Neel/Desktop/Google Pay - Neel")


time.sleep(3)
oc.driver.quit()