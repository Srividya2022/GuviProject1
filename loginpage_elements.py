from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time



class LoginPageElements:

    username_textbox_xpath = "//input[@name = 'username']"
    password_textbox_xpath = "//input[@name = 'password']"
    login_button_xpath = "//button[@type ='submit']"
    invalid_credential_text_xpath = "//p[@class ='oxd-text oxd-text--p oxd-alert-content-text']"


    def __init__(self,driver):
        self.driver = driver

    def enterusername(self,username):
        username_element = self.driver.find_element(By.XPATH,self.username_textbox_xpath).send_keys(username)

    def enterpassword(self, password):
        username_element = self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        loginbutton_element = self.driver.find_element(By.XPATH, self.login_button_xpath).click


    def invalidcredential(self):
        invalid_credential_element = self.driver.find_element(By.XPATH, self.invalid_credential_text_xpath)
        if invalid_credential_element.text == "Invalid credentials" :
            print("Invalid login TC - PASS")
        else:
            print("Invalid TC -FAIL")
    def validlogincheck(self):

        current_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        if self.driver.current_url  == current_url:
            print("Valid user -PASS - User has logged in successfully" )
        else:
            print("user not logged in")
