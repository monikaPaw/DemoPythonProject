from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ProductsPage:
    # Web Elements for Products page of application
    lbl_Products_xpath = "//span[text()='Products']"
    btn_AddToCart_id = "add-to-cart-sauce-labs-backpack"
    lnk_Cart_xpath = "//div[@id='shopping_cart_container']/a"
    btn_Checkout_id = "checkout"
    txt_FirstName_id = "first-name"
    txt_LastName_id = "last-name"
    txt_PostalCode_id = "postal-code"
    btn_Continue_id = "continue"
    lnk_BagPack_xpath = "//a[@id='item_4_title_link']/div"
    btn_Finish_id = "finish"
    lbl_CheckoutPage_xpath = "//span[text()='Checkout: Complete!']"
    msg_CompleteCheckout_xpath = "// h2[text() = 'THANK YOU FOR YOUR ORDER']"
    btn_Remove_id = "remove-sauce-labs-backpack"
    btn_AddToCartAll_xpath = "//button[text()='Add to cart']"
    btn_RemoveAll_xpath ="//button[text()='Remove']"

    def __init__(self, driver):
        self.driver = driver

    # Methods for operations to be performed on web element
    def isProductsTextPresent(self):
        return self.isVisible(self.lbl_Products_xpath)

    def addProductToCart(self):
        self.driver.find_element_by_id(self.btn_AddToCart_id).click()

    def navigateToCart(self):
        self.driver.find_element_by_xpath(self.lnk_Cart_xpath).click()

    def clickCheckOut(self):
        self.driver.find_element_by_id(self.btn_Checkout_id).click()

    def sendFirstName(self, firstname):
        self.driver.find_element_by_id(self.txt_FirstName_id).clear
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys(firstname)

    def sendLastName(self, lastname):
        self.driver.find_element_by_id(self.txt_LastName_id).clear
        self.driver.find_element_by_id(self.txt_LastName_id).send_keys(lastname)

    def sendPostalCode(self, postalcode):
        self.driver.find_element_by_id(self.txt_PostalCode_id).clear
        self.driver.find_element_by_id(self.txt_PostalCode_id).send_keys(postalcode)

    def clickContinue(self):
        self.driver.find_element_by_id(self.btn_Continue_id).click()

    def getProductName(self):
        productname = self.driver.find_element_by_xpath(self.lnk_BagPack_xpath)
        return productname.text

    def clickFinish(self):
        self.driver.find_element_by_id(self.btn_Finish_id).click()

    def verifyCheckoutPage(self):
        checkoutpage = self.driver.find_element_by_xpath(self.lbl_CheckoutPage_xpath)
        return checkoutpage.text

    def verifyProductCheckoutMessage(self):
        checkoutmsg = self.driver.find_element_by_xpath(self.msg_CompleteCheckout_xpath)
        return checkoutmsg.text

    def clickOnRemoveButton(self):
        self.driver.find_element_by_id(self.btn_Remove_id).click()

    def isProductPresent(self):
        try:
            self.driver.find_element_by_xpath(self.lnk_BagPack_xpath)
        except NoSuchElementException:
            return True
        return False

    def getAllProductsCount(self):
        count = self.driver.find_elements_by_xpath(self.btn_AddToCartAll_xpath)
        return len(count)

    def clickOnAddToCartButtonAll(self):
        self.driver.find_element_by_xpath(self.btn_AddToCartAll_xpath).click()

    def getRemoveCount(self):
        removecount = self.driver.find_elements_by_xpath(self.btn_RemoveAll_xpath)
        return len(removecount)






