from selenium.common.exceptions import NoSuchElementException

from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_Operations_On_Product:
    # Read data from config file using utility class methods
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_product_removal(self, setup):

        self.logger.info("******************Test_004_Operations_On_Product**************")
        self.logger.info("******************Verify Product removed from cart successfully **************")
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

        # Code for removal of product from cart
        self.pp.addProductToCart()
        self.driver.implicitly_wait(2)  # Added wait to see the progress
        self.logger.info("Product Added successfully to the cart")
        self.pp.navigateToCart()
        self.pp.clickOnRemoveButton()
        self.logger.info("Verify Product Removed from cart")
        # Verify Product is present in cart or not
        if self.pp.isProductPresent(): # If condition to verify getting true as element is not present
            self.logger.info("Product is successfully removed from cart")
            self.logger.info("*****************Test to remove Product  from cart is Passed **************")
            self.driver.close()
            assert True
        else:
            self.logger.info("Product is not removed from cart")
            self.logger.info("*****************Test to remove Product  from cart is Failed **************")
            self.driver.close()
            assert False
