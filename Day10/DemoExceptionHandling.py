from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.indusind.com/in/en/personal.html")

try:
    driver.find_element_by_xpath("//a[@class='close'])[3]").click()

except:
    print("Notification Handled")

driver.find_elements_by_xpath("//a[text()='About Us'])[1]").click()

