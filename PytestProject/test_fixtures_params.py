from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pytest

#@pytest.fixture(params=["chrome", "firefox"],scope='class')
#def init__driver(request):
#    if request.param == "chrome":
#        web_driver = webdriver.Chrome()
#    if request.param == "firefox":
#        web_driver = webdriver.Firefox()
#    request.cls.driver=web_driver
#    yield
#    web_driver.close()

@pytest.mark.usefixtures("init__driver")
class Base_Test:
        pass

class Test_Google(Base_Test):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
