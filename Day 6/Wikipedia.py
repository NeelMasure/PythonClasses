# from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time


driver= Chrome(ChromeDriverManager().install())

driver.get("https://www.wikipedia.org/")

# //TAGNAME[@Attribute = 'Value']/TAGNAME
lang= driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")

print("List of Language",len(lang))

for l in lang:
    print(l.text)

time.sleep(3)
driver.close()