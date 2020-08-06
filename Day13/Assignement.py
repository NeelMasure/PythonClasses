from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver= Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone XR 64 GB Yellow",Keys.ENTER)
driver.find_element_by_class_name('s-image').click()

time.sleep(7)

driver.get("https://www.flipkart.com")
driver.switch_to_window("https://www.flipkart.com")

driver.fin("//button[@class='_2AkmmA _29YdH8']").click()


# driver.find_element_by_class_name("//button[@class='_2AkmmA _29YdH8']")



















