from testCases.test_base import BaseTest
from pageObjects.LoginPage import LoginPage
from Config.config import TestData

class Test_Login(BaseTest):



    def test_login(self):
        self.lP = LoginPage(self.driver)
        self.lP.do_login(TestData.username, TestData.password)
        self.lP.get_list()









