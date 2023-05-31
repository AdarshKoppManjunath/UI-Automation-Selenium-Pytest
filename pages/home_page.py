from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
class HomePage:
    def __init__(self,driver,util_obj,test_step_name=None):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.home_page_url="https://www.aircanada.com/"
        self.test_data_file_name="home_page_test_data"
        self.test_step_name=test_step_name
        #Every page has a testdata json file and every json file has seperate test step data. location is determined by file name + @ + step name. 
        if test_step_name!=None:
             self.test_data_location=self.test_data_file_name+"@"+self.test_step_name
             self.test_data=self.util_obj.get_test_data(self.test_data_location)
        self.delay=30
        
    #website shows redirection popup if this is being opened in other countries.    
    def click_okay_for_redirection_popup(self):
        try:
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["page_redirection_from_home_page"])
            element = self.driver.find_element("xpath",self.locators_data["page_redirection_from_home_page"])
            element.click()
            time.sleep(2)
        except (NoSuchElementException,TimeoutException) as e:
            print("No redirection popup apperared.")
        
    def naviagte_to_signin_page(self):
        #home page is showing alert for redirection. This may not be appeared if website is being opened in Canada
        self.driver.get(self.home_page_url)
        self.click_okay_for_redirection_popup()
        #wait for sign in wrapper to appear and then click on it. 
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["signin_wrapper_home_page"])
        element = self.driver.find_element("xpath",self.locators_data["signin_wrapper_home_page"])
        element.click()
        #wait for sign in link to appear and then click on it.
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["signin_page_link_home_page"])
        element = self.driver.find_element("xpath",self.locators_data["signin_page_link_home_page"])
        element.click()
        
    def naviagte_to_create_account_page(self):
        self.naviagte_to_signin_page()
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["create_account_sigin_page"])
        element = self.driver.find_element("xpath",self.locators_data["create_account_sigin_page"])
        element.click()
    
    def navigate_to_fly_wrapper(self):
        self.click_okay_for_redirection_popup()
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["fly_home_page"])
        element = self.driver.find_element("xpath",self.locators_data["fly_home_page"])
        element.click()
    
    def navigate_to_flight_status(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["flight_status_home_page"])
        element = self.driver.find_element("xpath",self.locators_data["flight_status_home_page"])
        element.click()
    
    def input_flight_number(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["flight_status_flight_number_home_page"])
        self.driver.find_element("xpath",self.locators_data["flight_status_flight_number_home_page"]).send_keys(self.test_data["flight_number"])
    
    def check_flight_status(self):
        self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["flight_status_search_button_home_page"])
        element = self.driver.find_element("xpath",self.locators_data["flight_status_search_button_home_page"])
        element.click()
        
        
    
        
        
    
        
       