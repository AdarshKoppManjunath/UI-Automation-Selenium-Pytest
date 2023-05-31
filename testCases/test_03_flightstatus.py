import pytest
import time
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_03_HomePage:
    home_page_url="https://www.aircanada.com/"
    
    #verify if web app is running or not
    def test_home_page_title(self):
        self.driver.get(self.home_page_url)
        actual_title=self.driver.title
        assert actual_title=="Air Canada" , "AirCanada Web Application is not loaded."
        
    #verify if flight status is showing data for existing flight number
    def test_flight_status_positive(self):
        self.driver.get(self.home_page_url)
        home_page_obj=HomePage(self.driver,self.util_obj,"test_flight_status_positive")
        home_page_obj.navigate_to_fly_wrapper()
        home_page_obj.navigate_to_flight_status()
        home_page_obj.input_flight_number()
        home_page_obj.check_flight_status()
        time.sleep(10)
        if "No flights found; try changing your search criteria" in self.driver.page_source:
               assert False, "flight status page is not working"
               
    #verify if flight status is showing data for non existing flight number
    def test_flight_status_negative(self):
        self.driver.get(self.home_page_url)
        home_page_obj=HomePage(self.driver,self.util_obj,"test_flight_status_negative")
        home_page_obj.navigate_to_fly_wrapper()
        home_page_obj.navigate_to_flight_status()
        home_page_obj.input_flight_number()
        home_page_obj.check_flight_status()
        time.sleep(10)
        if "No flights found; try changing your search criteria" not in self.driver.page_source:
               assert False, "flight status page is showing data for non existing flight number"

    