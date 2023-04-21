from Config.config import TestData
from Logs.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from pageObjects.MyInfoPage import MyInfoPage


class Test_MyInfoPage(BaseTest):

    logger = LogGen.loggen()

    def test_myInfo(self):
        self.logger.info("*********** inside test_myinforpage ***************************")
        self.lp = LoginPage(self.driver)
        myinfo = self.lp.do_login(TestData.username, TestData.password)
        myinfo.goto_page()
        myinfo.click_edit()
        myinfo.edit_personalDetails()
