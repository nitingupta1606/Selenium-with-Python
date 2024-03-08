import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()
driver.get("https://www.linkedin.com/home")
email=driver.find_element(By.XPATH,"//*[@id='session_key']")
email.clear()
email.send_keys("abc@gmail.com")
print("Null value"email.text)
print(email.get_attribute('value'))


time.sleep(15)
