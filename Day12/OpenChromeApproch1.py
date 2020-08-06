from selenium.webdriver import Chrome
path= "C:\\Users\\Neel\\PycharmProjects\\Floyd\\Day12\\Drivers\\chromedriver.exe"
driver=Chrome(executable_path=path)

driver.get("https://www.google.com")