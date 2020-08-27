from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver= Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.tripadvisor.in/")
driver.find_element_by_xpath("//input[contains(@placeholder, 'Where to?')]").send_keys("Club Mahindra",Keys.ENTER)
club= driver.find_element_by_xpath("//*[text()='Club Mahindra Madikeri, Coorg']")

club.click()