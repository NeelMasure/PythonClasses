from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver= Chrome(ChromeDriverManager().install())

driver.get("https://www.flipkart.com/")

# m= driver.find_elements_by_xpath("//select[@class='_2aUbKa'Neel]