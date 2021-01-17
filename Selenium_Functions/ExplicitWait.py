from Day12 import OpenChrome as lp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Selenium_Functions import Generic as gs
import time


lp.driver.get("https://www.expedia.co.in/")
lp.driver.maximize_window()
lp.driver.implicitly_wait(30)


lp.driver.find_element_by_xpath("//span[text()='Flights']").click()

lp.driver.find_element_by_xpath("//span[text()='One-way']").click()

leave = lp.driver.find_element_by_xpath("//span[text()='Leaving from']")
gs.actionClick(lp.driver,leave)

lp.driver.find_element_by_xpath("//input[@id='location-field-leg1-origin']").send_keys("Spanish Town (VIJ-Virgin Gorda)",Keys.ENTER)

going =lp.driver.find_element_by_xpath("//span[text()='Going to']")
gs.actionClick(lp.driver,going)
time.sleep(2)

dest = lp.driver.find_element_by_css_selector("#location-field-leg1-destination")
gs.actionSendKeys(lp.driver,"Milan (MIL-All Airports)")

liDest= lp.driver.find_elements_by_xpath("//ul[@class='uitk-typeahead-results no-bullet']/li")
for li in liDest:
    if li.text =="Milan (MIL-All Airports)":
        gs.actionClick(lp.driver, li.click())
        break




lp.driver.find_element_by_xpath("//button[text()='Search']").click()


#
#
# button = lp.driver.find_element_by_xpath("(//button[@type='button' and starts-with(@class,'btn-secondary btn-action t-select-btn')])[1]")
#
# # driver, max time, polling,ignoreExceptions
# wait = WebDriverWait(lp.driver,60,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
#
# element = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@type='button'])[34]")))
# element.click()
#
#
# thanks = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'No thanks')]")))
# thanks.click()


time.sleep(3)
lp.driver.quit()