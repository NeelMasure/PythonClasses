from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

driver= Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")