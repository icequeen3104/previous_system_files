from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username") #self is a keyword with which "username_input" variable becomes global variable without which it will be only a local variable
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning@830$3mk2")
        self.driver.find_element(*self.sign_button).click()

