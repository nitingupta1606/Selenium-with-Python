from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
Serv_obj= Service("C:\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service = Serv_obj)

driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#Self node
Text=driver.find_element(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/self::a").text
print(Text)

#Parent
Text=driver.find_element(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/parent::td").text
print(Text)

#Child
Totalchild=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/child::td")
print(len(Totalchild))

#Ancestor
Ancestor=driver.find_element(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr").text
print(Ancestor)

#Descendant
Descendant=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/descendant::*")
print(len(Descendant))

#Following
following=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/following::*")
print(len(following))

#Following_sibling
following_sibling=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/following-sibling::*")
print(len(following_sibling))

#Preceding
Preceding=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/preceding::*")
print(len(Preceding))

#Preceding_Sibling
Preceding_Sibling=driver.find_elements(By.XPATH,"//a[contains(text (),'Max Healthcare Inst.')]/ancestor::tr/preceding-sibling::*")
print(len(Preceding_Sibling))



