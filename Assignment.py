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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
print("Application launched successfully")

# Test case ID: TC_Login_02
username_element = driver.find_element(By.XPATH,"//input[@name = 'username']")
password_element = driver.find_element(By.XPATH,"//input[@name = 'password']")
loginbutton_element = driver.find_element(By.XPATH,"//button[@type ='submit']")
          #login_success_element = driver.find_element(By.XPATH,"//span[@class ='oxd-topbar-header-breadcrumb']")
username ='Admin'
password ="assds"
username_element.send_keys(username)
password_element.send_keys(password)
loginbutton_element.click()
time.sleep(3)
invalidcredentail_message = driver.find_element(By.XPATH, "//p[@class ='oxd-text oxd-text--p oxd-alert-content-text']")
if invalidcredentail_message.text == 'Invalid credentials' :
   print('Test case ID: TC_Login_02 -Pass ' +  invalidcredentail_message.text)
else:
   print('Test case ID: TC_Login_02 - fail')
time.sleep(4)

driver.refresh()
time.sleep(4)

#TTest case ID: TC_Login_01

username_element1 = driver.find_element(By.XPATH,"//input[@name = 'username']")
password_element1 = driver.find_element(By.XPATH,"//input[@name = 'password']")
loginbutton_element1 = driver.find_element(By.XPATH,"//button[@type ='submit']")

username_element1.send_keys("Admin")
password_element1.send_keys("admin123")
loginbutton_element1.click()
time.sleep(3)
pim_element = driver.find_element(By.XPATH, "//a[@href ='/web/index.php/pim/viewPimModule']")
time.sleep(2)
if pim_element.is_displayed():
   print ('Test case ID: TC_Login_01 - PASS')
else:
   print('Test case ID: TC_Login_01 - FAIL')


#Test case ID: TC_PIM_01 :Add Employee
pim_element.click()

employpee_list_element = driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]")
time.sleep(2)
add_Employee_element = driver.find_element(By.XPATH, "//a[text() = 'Add Employee']").click()
time.sleep(2)
firstname_element = driver.find_element(By.XPATH, "//input[@name ='firstName']").send_keys('a')
time.sleep(2)
lastname_element = driver.find_element(By.XPATH, "//input[@name ='lastName']").send_keys('a')
time.sleep(2)
# employeeid_element = driver.find_element(By.XPATH,"//div[2]/div/div/div[2]/input")
# employeeid_element.clear()
# employeeid_element ='100'
employeesave_element =driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
# add_Employee_element.click()
# firstname_element.send_keys('a')
# lastname_element.send_keys('a')
# employeesave_element.click()
#x = driver.get_screenshot_as_file('a')
add_emp_successmsg = driver.find_element(By.XPATH, "//p[contains(.,'Successfully Saved')]")
print("Test case ID: TC_PIM_01 :Add Employee: -Employee Added successfully : PASS ")
time.sleep(3)


#..Test case ID: TC_PIM_02 -Edit employee

pim_element = driver.find_element(By.XPATH, "//a[@href ='/web/index.php/pim/viewPimModule']").click()
time.sleep(5)
edit_button_click = driver.find_element(By.XPATH, "//button[@type='button'][2]").click()
time.sleep(3)
edit_Empfirstname = driver.find_element(By.XPATH, "//input[@name ='firstName']").send_keys('a')
time.sleep(2)
edit_Emplastname = driver.find_element(By.XPATH, "//input[@name ='lastName']").send_keys('a')
time.sleep(2)

edit_save_click = driver.find_element(By.XPATH, "//button[@type='submit']").click()
#edit_successmessage =driver.find_element(By.XPATH,"//p[contains(.,'Successfully Saved')]")

print('Test case ID: TC_PIM_02 -Employee Edited Successfully')



# employeeid_element = driver.find_element(By.XPATH,"//input[@class="oxd-input oxd-input--active"][2]")
# employeeid_element.clear()
# employeeid_element ='100'
#
# createlogindetails = driver.find_element(By.XPATH, "//input[@type ='checkbox']").click()
# addphoto =driver.find_element(By.XPATH, "//div[@class ='employee-image-wrapper']")

#.Test case ID: TC_PIM_03 -Delete employee

employpee_list_element = driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]").click()
time.sleep(2)
delete_button = driver.find_element(By.XPATH,"//button[@class ='oxd-icon-button oxd-table-cell-action-space'][1]").click()
time.sleep(2)
deletebutton_click = driver.find_element(By.XPATH,"//button[contains(.,' Yes, Delete')]").click()
time.sleep(2)

deletedmessage = driver.find_element(By.XPATH,"//p[contains(.,'Successfully Deleted')]")
if deletedmessage.is_displayed():
   print("Test case ID: TC_PIM_03 deletedmessage.text")
