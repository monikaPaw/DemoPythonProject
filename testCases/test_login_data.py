import time

from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig


class Test_003_Data_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    def test_login_data(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows ", self.rows)
        lst_status = []  # list to store status of test cases

        # For loop to iterate through all data rows in XL sheet
        for r in range(2, self.rows + 1):
            # Read data from xl
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # Fill data which to application from xl
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Swag Labs"

            if act_title == exp_title:  # Match title of current page
                if self.exp == "Pass":
                    self.lp.clickLogOut()
                    self.driver.implicitly_wait(2)
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.driver.implicitly_wait(2)
                    lst_status.append("Pass")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            print("Login Data Driven test Passed")
            assert True
        else:
            print("Login Data Driven test Failed")
            assert False

        self.driver.close()
