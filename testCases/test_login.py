import pytest

from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    # Reading data from config file using utilities
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    lockeduser = ReadConfig.getLockedUsername()
    lockedusermessage = ReadConfig.getLockedUserMessage()

    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        # Test to validate title of application under test
        self.logger.info("******************Test_001_Login**************")
        self.logger.info("******************Verify Login Page Title **************")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            self.logger.info("Page title should be displayed as: Swag Labs")
            self.driver.close()
            self.logger.info("******************Login page title verify test is passed**************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******************Login page title verify test is failed**************")
            assert False

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_valid(self, setup):
        # Test to validate login functionality
        self.logger.info("*************Verifying Login test***************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("Page title should be displayed as: Swag Labs")
        self.lp.clickLogin()
        self.logger.info("Clicked on Login button")

        act_title = self.driver.title
        exp_title = "Swag Labs"

        if act_title == exp_title:
            self.driver.close()
            self.logger.info("Page title Displayed as:")
            self.logger.info("******************Login is successfully done.**************")
            self.logger.info("******************Complete login is Passed.**************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******************Login page test is failed**************")
            assert False

    def test_login_invalid(self, setup):
        # Test to validate invalid login scenario for locked user

        self.logger.info("******************Test_001_Login**************")
        self.logger.info("******************Test to validate logged out user**************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.lockeduser)
        self.lp.setPassword(self.password)
        self.logger.info("Username and password is entered...")
        self.lp.clickLogin()
        self.logger.info("Clicked on Login button...")

        self.logger.info("Verify logged out user message")
        loggedoutMessage = self.lp.verifyLoggedOutUserMessage()
        if loggedoutMessage == self.lockedusermessage:
            self.logger.info("Locked user message is displayed as expected")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            self.driver.close()
            self.logger.info("Locked user validation test is passed....")
            assert True
        else:
            self.logger.info("Locked user message is not displayed as expected")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            self.driver.close()
            self.logger.info("Locked user validation test is failed....")
            assert False
