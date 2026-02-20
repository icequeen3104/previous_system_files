from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

text_box = driver.find_element(By.ID, "tinymce")
text_box.click()
text_box.send_keys(Keys.CONTROL, "a")
text_box.send_keys(Keys.DELETE)
text_box.send_keys("Hello from Selenium")

driver.switch_to.default_content()
driver.quit()
