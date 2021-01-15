from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver= Chrome(ChromeDriverManager().install())

def val():
    v=driver()
    driver.get(input(""))
    val=v.get(driver)
    return val
