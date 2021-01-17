from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

ops= ChromeOptions()
ops.add_argument("--disable-notification")

ops.add_argument("--incognito")

ops.add_argument('--ignore-certificate-errors')
driver= Chrome(ChromeDriverManager().install(),options=ops)

driver.get("https://www.demo.guru99.com/")

driver.find_element_by_xpath("//input[@name='emailid']").send_keys("neelmasure@gmail.com")

driver.find_element_by_xpath("//input[@value='Submit']").click()