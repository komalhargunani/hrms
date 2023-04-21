import pytest as pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.chrome_executable_path)
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path=TestData.firefox_executable_path)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()



