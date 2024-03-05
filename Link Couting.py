from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php")
Link= driver.find_elements(By.TAG_NAME, "a")
print(len(Link))