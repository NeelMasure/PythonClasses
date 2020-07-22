from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Day11 import Generic as gs

driver= Chrome(ChromeDriverManager().install())
url=gs.getValue("TC001","url")
driver.get(url)

