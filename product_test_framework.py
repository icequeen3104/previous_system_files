import time #lec 83-86
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.login import LoginPage


def test_product_test_framework(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    loginPage.login()
    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart("Blackberry")


    # Perform login
    #driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    #driver.find_element(By.NAME, "password").send_keys("learning@830$3mk2")
    #driver.find_element(By.ID, "signInBtn").click()

    # Wait for the 'shop' link to be clickable before clicking
    shop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='shop']"))
    )
    shop_button.click()

    # Find all product cards
    products = driver.find_elements(By.XPATH, "//div[@class= 'card h-100']")

    # Loop through products and click on 'Blackberry'
    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

    # Checkout process
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.ID, "country").send_keys("ind")

    # Wait for 'India' to appear and click it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()

    # Agree to terms and submit
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

    # Verify success message
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success!" in successText, f"Expected success message but got: {successText}"

    driver.quit()  # Close the browser
