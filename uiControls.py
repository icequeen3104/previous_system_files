#for checkingboxes,radio buttons
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type= 'checkbox']")
print(len(checkboxes))

#for ticking the checkboxes
#for checkbox in checkboxes:
#    if checkbox.get_attribute("value") == "option2":
#        checkbox.click()
#        assert checkbox.is_selected()
#        break

#selecting the radio buttons
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[0].click()
#assert radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(2)