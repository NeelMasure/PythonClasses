from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver= Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in")
driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone xr 128gb black",Keys.ENTER)
phone = driver.find_element_by_xpath("//*[text()='Apple iPhone 11 (64GB) - Black']")
phone.click()

time.sleep(7)

driver.get("https://www.flipkart.com")
driver.find_element_by_xpath("//button[contains(@class,'_2AkmmA _29YdH8')]").click()

try : driver.switch_to_window("https://www.flipkart.com");

except: "Exception handled"

driver.find_element_by_name("q").send_keys("Iphone XR 64 GB Yellow",Keys.ENTER)
driver.find_element_by_xpath("//*[text()='Apple iPhone 11 (Yellow, 64 GB)']").click()




















