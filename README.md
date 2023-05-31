# tucowss_assesment
To run this, either you github action workflow or clone the repo and install the required libraries from requirements.txt, and type pytest in cmd. 

pages- has POM for UI pages

testCases- has conftest ( setup for all testcases ) and test cases

testData- has testcase json file and each json file has test data for test step. 

utilities- has locators.json which covers all xpath referred  and utils.py ( object is created only once during conftest setup and
shared across everywhere through test case to fetch locators, test data and for some common functions 
