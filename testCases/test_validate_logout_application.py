import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_006_Validate_Logout:
    # Read data from config file using utility class methods
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_log_out_validate(self, setup):
        self.logger.info("******************Test_006_Validate_Logout**************")
        self.logger.info("******************Verify user get logged out successfully **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)  # Object of login page to access there methods and webElements
        self.pp = ProductsPage(self.driver)  # Object of Products page to access there methods and webElements
        self.logger.info("User name and password has been entered")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("Page title should be displayed as: Swag Labs")
        self.lp.clickLogin()
        self.logger.info("Clicked on Login button")

        # logout from the application
        self.logger.info('Logout from the application.')
        self.lp.clickLogOut()
        self.logger.info('Successfully Logged out from the application.')

        # Verify user navigate back to login page
        act_title = self.driver.title
        exp_title = "Swag Labs"

        if act_title == exp_title:
            self.driver.close()
            self.logger.info("Page title Displayed as:")
            self.logger.info("******************User Logged out successfully.**************")
            self.logger.info("******************Log out test is Passed.**************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******************Log out test Failed**************")
            assert False













