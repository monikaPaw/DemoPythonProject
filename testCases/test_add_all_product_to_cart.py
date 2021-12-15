from selenium.common.exceptions import NoSuchElementException
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductsPage import ProductsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_Add_All_Product_To_Cart:
    # Read data from config file using utility class methods
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_add_all_products_to_cart(self, setup):

        self.logger.info("******************Test_005_Add_All_Product_To_Cart**************")
        self.logger.info("******************Verify All product added to cart successfully **************")
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

        # Add all products from products page
        # iterate through each user by using the index
        productnum = self.pp.getAllProductsCount()
        print(productnum)

        # Click on all Add to cart button on products page
        for r in range(0, productnum):
            print(productnum)
            self.pp.clickOnAddToCartButtonAll()
            self.driver.implicitly_wait(1)

        self.pp.navigateToCart()
        self.logger.info("All Products are added to cart ")

        # Code to verify number of products added are equal to number of product available on page On Our ecommerce
        # application total number of product is not available so I am getting number of remove button and matching
        # it with number of added Products
        # Get Remove button count as we don't have total number of products in cart
        expproductcount = self.pp.getRemoveCount()
        print(expproductcount)
        if expproductcount == productnum:
            self.logger.info("All product added count is matched expected count")
            self.driver.close()
            assert True
        else:
            self.logger.info("All product added count is not matched expected count")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Locked_User_Validation.png")
            self.driver.close()
            assert False








