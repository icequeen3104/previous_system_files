import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CSSSelector, Classname, name, linkTest
#driver.find_element(By.NAME, "name").send_keys("saujanya")
driver.find_element(By.NAME, "email").send_keys("saujanya.310104@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#Xpath = //tagname[@attribute= 'value'] -> //input[@type= 'submit']
#CSS = //tagname[attribute= 'value'] -> //input[@type= 'submit'], #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("saujanya")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type= 'submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
#static dropdrown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female") #then the option "female" in the dropdown list will get selected
#dropdown = select_by_index(0) #then the option will be selected by index first, second, third.... --> 0,1,2,3.....
dropdown = select_by_value()
driver.find_element(By.XPATH, "(//input[@type= 'text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type= 'text'])[3]").clear()
time.sleep(20)
driver.quit()