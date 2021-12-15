import time
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_Order_Product_E2E:

    # Read data from config file using utility class methods
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstName()
    lastname = ReadConfig.getLastName()
    postalcode = ReadConfig.getPostalCode()
    checkoutmessage = ReadConfig.getCheckoutMessage()

    logger = LogGen.loggen()

    def test_order_product(self, setup):
        self.logger.info("******************Test_003_Order_Product_E2E**************")
        self.logger.info("******************Verify Order placed successfully **************")
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

        # Code for end to end order placement
        self.pp.addProductToCart()
        self.logger.info("Product Added successfully to the cart")
        self.pp.navigateToCart()
        self.pp.clickCheckOut()
        self.pp.sendFirstName(self.firstname)
        self.pp.sendLastName(self.lastname)
        self.pp.sendPostalCode(self.postalcode)
        self.pp.clickContinue()

        act_product = self.pp.getProductName()
        # Verify Proper product is added to the cart
        self.logger.info("Verify Proper product is getting checkout")
        exp_product = "Sauce Labs Backpack"
        if act_product == exp_product:
            self.logger.info('Expected product is present at the checkout')
            assert True
        else:
            self.logger.info("Expected product is not present at the checkout")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            assert False

        self.pp.clickFinish()

        # Verify Complete checkout message
        self.logger.info("Verify complete checkout page loaded")

        act_checkoutpage= self.pp.verifyCheckoutPage()
        print(act_checkoutpage)
        exp_checkoutpage = "CHECKOUT: COMPLETE!"
        if act_checkoutpage == exp_checkoutpage:
            self.logger.info('Successfully placed order for the product.')
            assert True
        else:
            self.logger.info("Product order in not successful.")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            assert False

        # Verify message on checkout page
        act_checkoutmsg= self.pp.verifyProductCheckoutMessage()
        print(act_checkoutmsg)
        if self.checkoutmessage == act_checkoutmsg:
            self.logger.info('Checkout page message is displayed as expected.')
            assert True
        else:
            self.logger.info('Checkout page message is displayed as expected.')
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            False

        # logout from the application
        self.logger.info('Logout from the application.')
        self.lp.clickLogOut()
        self.logger.info('Successfully Logged out from the application.')
        self.driver.close()












