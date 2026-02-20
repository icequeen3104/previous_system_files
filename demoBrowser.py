import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("/Users/rahulshetty/documents/chromedriver")
#driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
time.sleep(2)