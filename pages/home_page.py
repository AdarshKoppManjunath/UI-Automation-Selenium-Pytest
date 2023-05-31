from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
class HomePage:
    def __init__(self,driver,util_obj):
        self.driver=driver
        self.util_obj=util_obj
        self.locators_data=self.util_obj.get_locators_data()
        self.home_page_url="https://www.aircanada.com/"
        self.delay=30
        
    def naviagte_to_signin_page(self):
        #home page is showing alert for redirection. This may not be appeared if website is being opened in Canada
        self.driver.get(self.home_page_url)
        try:
            self.util_obj.explict_wait_unitl_element_found(self.delay,By.XPATH,self.locators_data["page_redirection_from_home_page"])
            element = self.driver.find_element("xpath",self.locators_data["page_redirection_from_home_page"])
            element.click()
        except (NoSuchElementException,TimeoutException) as e:
            print("No redirection popup apperared.")
        #wait for sign in wrapper to appear and then click on it. 
        time.sleep(2)
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
       