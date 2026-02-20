import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])

time.sleep(2)
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(windowsOpened[1])
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text
