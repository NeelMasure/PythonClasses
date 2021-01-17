from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver= Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.save_screenshot("Screenshot.png")
time.sleep(3)
driver.close()



