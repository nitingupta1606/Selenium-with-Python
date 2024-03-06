from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php")
driver.find_element(By.XPATH, "//*[@id='search_query_top' or @name='search_query']").send_keys("Tshirt")
driver.find_element(By.XPATH,"//button[@name='submit_search' and @class='btn btn-default button-search']").click()