import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class Test_002_DDT_Login:
    # Reading data from config file using utilities
    baseURL = ReadConfig.getApplicationURL()
    # Test data file path to read data for data driver test cases
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        # Test to validate login functionality for multiple user from xl sheet
        self.logger.info("****************Test_002_DDT_Login********************")
        self.logger.info("****************Verifying Login DDT (Data Driven test)********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Page title should be displayed as: Swag Labs")

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows ", self.rows)
        lst_status = []  # Empty array to store status of test case

        self.logger.info("Reading Data from XL sheet to verify login.")

        # Code to Read data from XL file
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.logger.info("Entering username and password which is taken from XL")
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Swag Labs"

            if act_title == exp_title:  # Match title of current page
                if self.exp == "Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Pass")
            self.driver.close()
            assert True
        else:
            self.logger.info("Fail")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            self.driver.close()
            assert False
