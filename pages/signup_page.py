from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class SignUp:
    
    def __init__(self,driver,util_obj,test_step_name):
        self.driver=driver
        self.util_obj=util_obj
        #allocating a seperate test data json file for every page. In this case, 'signin_page_test_data.json' is for sigin page.
        self.test_data_file_name="signup_page_test_data"
        self.test_step_name=test_step_name
        #Every page has a testdata json file and every json file has seperate test step data. location is determined by file name + @ + step name. 
        self.test_data_location=self.test_data_file_name+"@"+self.test_step_name
        self.test_data=self.util_obj.get_test_data(self.test_data_location)
        self.locators_data=self.util_obj.get_locators_data()
        self.delay=60
        
    def input_email(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["email_signup_page"])
        self.driver.find_element("xpath",self.locators_data["email_signup_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["email_signup_page"]).send_keys(self.test_data["email"])
    
    def input_password(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["password_signup_page"])
        self.driver.find_element("xpath",self.locators_data["password_signup_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["password_signup_page"]).send_keys(self.test_data["password"])
    
    def check_box(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.CSS_SELECTOR,self.locators_data["checkbox_signup_page"])
        self.driver.find_element(By.CSS_SELECTOR,self.locators_data["checkbox_signup_page"]).click()
        
    def continue_button(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["continue_signup_page"])
        self.driver.find_element("xpath",self.locators_data["continue_signup_page"]).click()
        time.sleep(10)
    
    def input_firstname(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["firstname_signup_page"])
        self.driver.find_element("xpath",self.locators_data["firstname_signup_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["firstname_signup_page"]).send_keys(self.test_data["firstName"])
        
    def input_lastname(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["lastname_signup_page"])
        self.driver.find_element("xpath",self.locators_data["lastname_signup_page"]).clear()
        self.driver.find_element("xpath",self.locators_data["lastname_signup_page"]).send_keys(self.test_data["lastName"])
    
    def input_gender(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["gender_frame_signup_page"])
        self.driver.find_element("xpath",self.locators_data["gender_frame_signup_page"]).click()
        locator=self.locators_data["gender_signup_page"].replace("'gender'","'%s'"%(self.test_data["gender"]))
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,locator)
        self.driver.find_element("xpath",locator).click()
        
    def input_birth_date(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["birth_date_frame_signup_page"])
        self.driver.find_element("xpath",self.locators_data["birth_date_frame_signup_page"]).click()
        locator=self.locators_data["birth_date_signup_page"].replace("'date'","%s"%(self.test_data["birth_date"]))
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,locator)
        self.driver.find_element("xpath",locator).click()
    
    def input_birth_month(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["birth_month_frame_signup_page"])
        self.driver.find_element("xpath",self.locators_data["birth_month_frame_signup_page"]).click()
        locator=self.locators_data["birth_month_signup_page"].replace("'month'","'%s'"%(self.test_data["birth_month"]))
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,locator)
        self.driver.find_element("xpath",locator).click()
    
    def input_birth_year(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["birth_year_frame_signup_page"])
        self.driver.find_element("xpath",self.locators_data["birth_year_frame_signup_page"]).click()
        locator=self.locators_data["birth_year_signup_page"].replace("'year'","%s"%(self.test_data["birth_year"]))
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,locator)
        self.driver.find_element("xpath",locator).click()
        
        
        
  
        
    