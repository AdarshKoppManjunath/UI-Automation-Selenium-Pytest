import os
import json
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:
    def __init__(self,driver):
        self.driver=driver
    #explicit wait when page is taking way too long to load. 
    def explict_wait_unitl_element_found(self,delay,locator_type,locator):
        element = WebDriverWait(self.driver, delay).until(
        EC.presence_of_element_located((locator_type,locator))
    )
    #get all locators data from the locators.json file.
    def get_locators_data(self):
        locator_path=os.path.join("utilities","locators.json")
        file=open(locator_path)
        locator_data=json.load(file)
        return locator_data
    #get test data using test file and step name. 
    def get_test_data(self,test_file_step):
        testcase,step=test_file_step.split("@")
        locator_path=os.path.join("testData",testcase+".json")
        file=open(locator_path)
        test_data=json.load(file)
        return test_data[step]
        

        