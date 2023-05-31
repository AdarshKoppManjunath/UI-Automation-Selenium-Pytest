import pytest
from utilities.utils import Utils
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium import webdriver
import chromedriver_autoinstaller 
chromedriver_autoinstaller.install() 


@pytest.fixture()
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #to enable automation. Site blocks login automation. 
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"] )
    chrome_options.add_experimental_option("useAutomationExtension", False)
    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    request.cls.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    request.cls.util_obj =Utils(request.cls.driver)
    yield request.cls.driver
    request.cls.driver.close()