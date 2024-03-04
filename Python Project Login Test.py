import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
import time

driver.get("https://www.linkedin.com/home")


driver.find_element(By.ID,"session_key").send_keys("nitingupta01997@gmail.com")
driver.find_element(By.ID,"session_password").send_keys("")
driver.find_element(By.XPATH,"//*[@id='main-content']/section[1]/div/div/form/div[2]/button").click()
time.sleep(25)

