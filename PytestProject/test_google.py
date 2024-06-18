from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pytest

driver = None

def setup(module):
    global driver
    #s = Service('/Users/ysrinivas/PycharmProjects/PythonSeleniumSessions/Drivers/chromedriver 2')
    #driver = webdriver.Chrome(service=s)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown(module):
    driver.quit()


def test_google():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "google.com"
