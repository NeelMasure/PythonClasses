from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver= Chrome(ChromeDriverManager().install())

driver.get("https://www.wikipedia.org/")

lang= driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")


for l in lang:
    print(l.text)
