from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
from GuviOrangeHrmProject.PageObjects.loginpage_elements import LoginPageElements
from GuviOrangeHrmProject.PageObjects.pim_emp_page_elements import EmployeePageElements

class OrangehrmTest(unittest.TestCase):

     @classmethod
     def setUpClass(cls) -> None:
         cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
         cls.driver.implicitly_wait(10)
         cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         print("Application launched successfully")
         cls.driver.maximize_window()
         print('Chrome Browser launched')

     def test_invalidlogin(self):
         driver =self.driver
         invalidlogin = LoginPageElements(driver)
         invalidlogin.enterusername("Admin")
         invalidlogin.enterpassword("123")
         time.sleep(2)
         invalidlogin.click_login()
         time.sleep(2)
         invalidlogin.invalidcredential()
         time.sleep(3)
         driver.refresh()

     def test_validlogin(self):
         driver = self.driver
         validlogin = LoginPageElements(driver)
         validlogin.enterusername("Admin")
         validlogin.enterpassword("admin123")
         validlogin.click_login()
         validlogin.validlogincheck()

     def add_employee(self):
         driver = self.driver
         employeeadd = EmployeePageElements(driver)
         employeeadd.pimclick()
         employeeadd.emplist_click()
         employeeadd.add_employee_button()
         employeeadd.add_empfirstname_enter("aaa")
         employeeadd.add_emplastname_enter("bbb")
         employeeadd.empsavebutton_click()
         print("Employee added successfully ")

     def edit_employee(self):
         driver = self.driver
         employeeedit = EmployeePageElements(driver)
         employeeedit.pimclick()
         employeeedit.emplist_click()
         employeeedit.edit_image_click()
         employeeedit.edit_empfirstname_enter("updated")
         employeeedit.edit_emplastname_enter("updated")
         employeeedit.edit_emp_save_click()
         print("Employee updated successfully ")

     def delete_employee(self):
         driver = self.driver
         employee_delete = EmployeePageElements(driver)
         employee_delete.emplist_click()
         employee_delete.delete_click()
         employee_delete.delete_emp_successmsg()


     @classmethod
     def tearDownClass(cls) -> None:
         cls.driver.close()
         cls.driver.quit()
         print("Test done")






























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
# driver.implicitly_wait(10)
# print("Application launched successfully")
# username_element = driver.find_element(By.XPATH,"//input[@name = 'username']")
# password_element = driver.find_element(By.XPATH,"//input[@name = 'password']")
# loginbutton_element = driver.find_element(By.XPATH,"//button[@type ='submit']")
#           #login_success_element = driver.find_element(By.XPATH,"//span[@class ='oxd-topbar-header-breadcrumb']")
# username ='Admin'
# password ="assds"
# username_element.send_keys(username)
# password_element.send_keys(password)
# loginbutton_element.click()
# time.sleep(3)
# x = driver.find_element(By.XPATH, "//p[@class ='oxd-text oxd-text--p oxd-alert-content-text']")
#
# print(x.text)
#
#
#
#
# time.sleep(4)
#
# driver.refresh()
# time.sleep(4)
#
# username_element1 = driver.find_element(By.XPATH,"//input[@name = 'username']")
# password_element1 = driver.find_element(By.XPATH,"//input[@name = 'password']")
# loginbutton_element1 = driver.find_element(By.XPATH,"//button[@type ='submit']")
#
# username_element1.send_keys("Admin")
# password_element1.send_keys("admin123")
# loginbutton_element1.click()
# time.sleep(3)
# print('The user is logged in successfully.')
#
#
# pim_element = driver.find_element(By.XPATH, "//a[@href ='/web/index.php/pim/viewPimModule']").click()
# time.sleep(2)
# employpee_list_element = driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]")
# time.sleep(2)
# add_Employee_element = driver.find_element(By.XPATH, "//a[text() = 'Add Employee']").click()
# time.sleep(2)
# firstname_element = driver.find_element(By.XPATH, "//input[@name ='firstName']").send_keys('a')
# time.sleep(2)
# lastname_element = driver.find_element(By.XPATH, "//input[@name ='lastName']").send_keys('a')
# time.sleep(2)
# employeesave_element =driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(2)
# # add_Employee_element.click()
# # firstname_element.send_keys('a')
# # lastname_element.send_keys('a')
# # employeesave_element.click()
# #x = driver.get_screenshot_as_file('a')
# add_emp_successmsg = driver.find_element(By.XPATH, "//p[contains(.,'Successfully Saved')]")
# print("user saved")
# time.sleep(3)
#
# #..edit employee
#
# pim_element = driver.find_element(By.XPATH, "//a[@href ='/web/index.php/pim/viewPimModule']").click()
# time.sleep(5)
# edit_button_click = driver.find_element(By.XPATH, "//button[@type='button'][2]").click()
# time.sleep(3)
# edit_Empfirstname = driver.find_element(By.XPATH, "//input[@name ='firstName']").send_keys('a')
# time.sleep(2)
# edit_Emplastname = driver.find_element(By.XPATH, "//input[@name ='lastName']").send_keys('a')
# time.sleep(2)
#
# edit_save_click = driver.find_element(By.XPATH, "//button[@type='submit']").click()
# #edit_save_click = driver.find_element(By.XPATH, "//button[@class ='oxd-icon-button oxd-table-cell-action-space'][2]").click()
# time.sleep(2)
# #edit_successmessage =driver.find_element(By.XPATH,"//p[contains(.,'Successfully Saved')]")
#
# print('edited')
#
#
#
# # employeeid_element = driver.find_element(By.XPATH,"//input[@class="oxd-input oxd-input--active"][2]")
# # employeeid_element.clear()
# # employeeid_element ='100'
# #
# # createlogindetails = driver.find_element(By.XPATH, "//input[@type ='checkbox']").click()
# # addphoto =driver.find_element(By.XPATH, "//div[@class ='employee-image-wrapper']")
#
# #....delete...
# employpee_list_element = driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]").click()
# time.sleep(2)
# delete_button = driver.find_element(By.XPATH,"//button[@class ='oxd-icon-button oxd-table-cell-action-space'][1]").click()
# time.sleep(2)
# deletebutton_click = driver.find_element(By.XPATH,"//button[contains(.,' Yes, Delete')]").click()
# time.sleep(2)
#
# x = driver.find_element(By.XPATH,"//p[contains(.,'Successfully Deleted')]")
# if x.is_displayed():
#    print(x.text)
