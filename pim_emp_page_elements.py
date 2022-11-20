from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time


class EmployeePageElements:

    pim_element_xpath = "//a[@href ='/web/index.php/pim/viewPimModule']"
    employpee_list_xpath = "//a[contains(text(),'Employee List')]"
    add_employee_button_xpath = "//a[text() = 'Add Employee']"
    firstname_textbox_xpath = "//input[@name ='firstName']"
    lastname_textbox_xpath = "//input[@name ='lastName']"
    empsave_button_xpath = "//button[@type='submit']"
    add_emp_successmsg_xpath = "//p[contains(.,'Successfully Saved')]"
    edit_image_xpath = "//button[2]/i"
    edit_Empfirstname_textbox_xpath = "//input[@name ='firstName']"
    edit_Emplastname_textbox_xpath = "//input[@name ='lastName']"
    edit_emp_save_xpath =  "//button[@type='submit']"
    edit_emp_successmessage_xpath = "//p[contains(.,'Successfully Saved')]"
    delete_button_xpath ="//button[@class ='oxd-icon-button oxd-table-cell-action-space'][1]"
    delete_success_msg_xpath = "//button[contains(.,' Yes, Delete')]"

    def __init__(self,driver):
        self.driver = driver

    def pimclick(self):
        pim_click_element = self.driver.find_element(By.XPATH,self.pim_element_xpath)
        pim_click_element.click

    def emplist_click(self):
        employpee_list_element = self.driver.find_element(By.XPATH,self.employpee_list_xpath).click()

    def add_employee_button(self):
        add_Employee_button_element = self.driver.find_element(By.XPATH,self.add_employee_button_xpath).click()

    def add_empfirstname_enter(self, addusername):
        add_empfirstname_element = self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(addusername)

    def add_emplastname_enter(self, addlastname):
        add_emplastname_element = self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(addlastname)

    def empsavebutton_click(self):
        employeesave_element = self.driver.find_element(By.XPATH,self.empsave_button_xpath).click()

    def addemp_successmessage(self):
        add_emp_successmsg_element = self.driver.find_element(By.XPATH,self.add_emp_successmsg_xpath)

    def edit_image_click(self):
        edit_image_element = self.driver.find_element(By.XPATH, self.edit_image_xpath).click()

    def edit_empfirstname_enter(self,editusername):
        edit_empfirstname_element = self.driver.find_element(By.XPATH, self.edit_Empfirstname_textbox_xpath).send_keys(editusername)

    def edit_emplastname_enter(self,editlastname):
        editlastname_element = self.driver.find_element(By.XPATH, self.edit_Empfirstname_textbox_xpath).send_keys(editlastname)

    def edit_emp_save_click(self):
        edit_empsave_element = self.driver.find_element(By.XPATH, self.edit_emp_save_xpath).click()

    def edit_emp_successmsg(self):
        edit_empsace_success_element = self.driver.find_element(By.XPATH, self.edit_emp_successmessage_xpath)

    def delete_click(self):
        delete_emp_element = self.driver.find_element(By.XPATH, self.delete_button_xpath).click()

    def delete_emp_successmsg(self):
        delete_emp_success_element = self.driver.find_element(By.XPATH, self.delete_success_msg_xpath)


