from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()
driver.get("https://text-compare.com/")
driver.find_element(By.XPATH,"//*[@id='inputText1']").send_keys("Welcome to selenium")

#Importing ActionChains clss
act=ActionChains(driver)

#select element
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#Copy the Element
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Tab Key
act.send_keys(Keys.TAB).perform()

#Pasting
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()





















