from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
Serv_Obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service=Serv_Obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
#Xpath= driver.find_elements(By.XPATH,"//*[@id='maintext']//ul//a")
Tagname= driver.find_elements(By.TAG_NAME,"a")

#print(len(Xpath))
print(len(Tagname)) #48

#printing links list
# for links in Tagname:
#     print(links.text)

#Checking Broken links:
for links in Tagname:
    url= links.get_attribute('href')
    try:
        res= requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, "Broken link")
    else:
        print(url, "Valid links")
