import time


class LoginPage:
    # Web elements for login page. WebElement name specify type of element then field name and attribute used for"""
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_openmenu_id = "react-burger-menu-btn"
    link_logout_id = "logout_sidebar_link"
    msg_loggedout_xpath = "//*[@id='login_button_container']/div/form/div[3]"
    lbl_Products_xpath = "//span[text()='Products']"

    def __init__(self, driver):
        self.driver = driver
    # Methods for operations to be performed on web elements on the page

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickLogOut(self):
        self.driver.find_element_by_id(self.button_openmenu_id).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.link_logout_id).click()

    def verifyLoggedOutUserMessage(self):
        msgloggedout = self.driver.find_element_by_xpath(self.msg_loggedout_xpath)
        return msgloggedout.text

    def getProductLabel(self):
        label = self.driver.find_element_by_xpath(self.lbl_Products_xpath)
        return label.text




