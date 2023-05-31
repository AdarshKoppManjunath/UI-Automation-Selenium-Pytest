import pytest
from pages.home_page import HomePage
from pages.signin_page import SignIn
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_01_Signin:
    home_page_url="https://www.aircanada.com/"

    def test_home_page_title(self):
        self.driver.get(self.home_page_url)
        actual_title=self.driver.title
        assert actual_title=="Air Canada" , "AirCanada Web Application is not loaded."
            
    #login page direct link is keep redirecting to homepage for me. So navigating to login from homepage
    def test_signin_positive(self):
       home_page_obj=HomePage(self.driver,self.util_obj)
       home_page_obj.naviagte_to_signin_page()
       signin_page_obj=SignIn(self.driver,self.util_obj,"test_signin_positive")
       signin_page_obj.input_user_name()
       signin_page_obj.input_user_password()
       signin_page_obj.click_signin()
       if "verification code" not in self.driver.page_source:
           assert False, "Activation Code Request should be displayed after login"
    
    def test_signin_negative(self):
       home_page_obj=HomePage(self.driver,self.util_obj)
       home_page_obj.naviagte_to_signin_page()
       signin_page_obj=SignIn(self.driver,self.util_obj,"test_signin_negative")
       signin_page_obj.input_user_name()
       signin_page_obj.input_user_password()
       signin_page_obj.click_signin()
       if "verification code" in self.driver.page_source:
               assert False, "Login should not work with invalid credentials"
       
       
     
      