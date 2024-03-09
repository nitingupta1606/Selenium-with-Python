from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()

mywait=WebDriverWait(driver,10)

driver.get("https://www.google.co.in/")
Serach= driver.find_element(By.XPATH,"//*[@id='APjFqb']")
Serach.send_keys("Selenium")
Serach.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
