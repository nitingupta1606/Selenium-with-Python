from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.google.co.in/")
Serach= driver.find_element(By.XPATH,"//*[@id='APjFqb']")
Serach.send_keys("Selenium")
Serach.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()


