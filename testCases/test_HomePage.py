from Logs.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from Utility.locators import LoginPageLocators
from Config.config import TestData
from pageObjects.HomePage import HomePage



class Test_HomePage(BaseTest):

    logger = LogGen.loggen()

    def test_homepage(self):
        self.logger.info("*********** inside test_homepage ***************************")
        self.lp = LoginPage(self.driver)
        homepage = self.lp.do_login(TestData.username, TestData.password)
        title = homepage.get_homePageTitle(TestData.homepagetitile)
        assert title == TestData.homepagetitile
        print("title of webpage:", title)
        print("is calendar exist on webpage:", homepage.is_calendar_exist())
        print("header of R&R section:", homepage.is_RR_isVisible())
        print("today's birthday list:", homepage.get_birthdayList())
        print("column's present in my leaves table:", homepage.get_leaveBalanceColumnName())
        print("details of leaves, leave type and its count:", homepage.get_leaveBalanceRows())
        print("today's date:", homepage.get_todayDate())
        print("list of people for R&RVideos:", homepage.get_RAndRVideosList())
        homepage.verify_todayDate()





