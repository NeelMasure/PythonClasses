from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
ops = ChromeOptions()
# https://chromedriver.chromium.org/capabilities
# https://stackoverflow.com/questions/38335671/where-can-i-find-a-list-of-all-available-chromeoption-arguments

ops.add_argument("--disable-notifications")
driver= Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.in/")
driver.maximize_window()
tag = driver.find_elements_by_tag_name("a")
print("Total links :", len(tag))


for link in tag:
        print(link.text + "-----"+ link.get_attribute("href"))

driver.quit()