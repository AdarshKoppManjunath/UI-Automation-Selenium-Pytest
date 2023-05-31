from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
class SignIn:
    input_username_name="username"
    input_password_name="password"
    
    def __init__(self,driver,util_obj,test_step_name):
        self.driver=driver
        self.util_obj=util_obj
        #allocating a seperate test data json file for every page. In this case, 'signin_page_test_data.json' is for sigin page.
        self.test_data_file_name="signin_page_test_data"
        self.test_step_name=test_step_name
        #Every page has a testdata json file and every json file has seperate test step data. location is determined by file name + @ + step name. 
        self.test_data_location=self.test_data_file_name+"@"+self.test_step_name
        self.test_data=self.util_obj.get_test_data(self.test_data_location)
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
        
    def input_user_name(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["username_signin_page"])
        self.driver.find_element("xpath",self.locators_data["username_signin_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["username_signin_page"]).send_keys(self.test_data["username"])
    
    def input_user_password(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["password_signin_page"])
        self.driver.find_element("xpath",self.locators_data["password_signin_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["password_signin_page"]).send_keys(self.test_data["password"])
    
    def click_signin(self):
        time.sleep(3) #this is because site blocks automation. To avoid, set some sleep after password and automation enable flags are added in conftest file
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["button_signin_signin_page"])
        self.driver.find_element("xpath",self.locators_data["button_signin_signin_page"]).send_keys(Keys.ENTER)
        time.sleep(10)
   
        
    