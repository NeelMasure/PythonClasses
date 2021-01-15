from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

ops= ChromeOptions()
ops.add_argument("--disable-notification")

ops.add_argument("--incognito")

ops.add_argument('--ignore-certificate-errors')

driver= Chrome(ChromeDriverManager().install(),options=ops)

driver.maximize_window()
driver.get("https://www.demo.guru99.com/")

driver.find_element_by_xpath("//a[text()='Telecom Project']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Add Customer']").click()
time.sleep(3)
driver.find_element_by_xpath("//label[text()='Done']").click()
time.sleep(3)
driver.find_element_by_id("fname").send_keys("Suraj")
time.sleep(3)
driver.find_element_by_id("lname").send_keys("Masure")
time.sleep(3)
driver.find_element_by_id("email").send_keys("neelmasure@gmail.com")
time.sleep(3)

scdown = driver.find_element_by_xpath("//input[@name='submit']")

op.driver.execute_script("arguments[0].scrollIntoView();",scdown)

driver.find_element_by_id("message").send_keys("House No 02 Chichwade Chawl Back of Arti Center Pune =411033")
time.sleep(3)
mobile = driver.find_element_by_name("telephoneno").send_keys("454526486")


for m in mobile:
    m(len())
    print(len())
    break

time.sleep(3)

driver.quit()