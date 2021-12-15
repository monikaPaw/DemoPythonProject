import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    # Static methods to get data from config.ini file
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def getFirstName():
        firstname = config.get('customer details', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('customer details', 'lastname')
        return lastname

    @staticmethod
    def getPostalCode():
        postalcode = config.get('customer details', 'postalcode')
        return postalcode

    @staticmethod
    def getCheckoutMessage():
        checkoutmessage = config.get('messages', 'checkoutmessage')
        return checkoutmessage

    @staticmethod
    def getLockedUsername():
        lockedusername = config.get('common data', 'lockeduser')
        return lockedusername

    @staticmethod
    def getLockedUserMessage():
        lockedusermessage = config.get('messages', 'lockedoutusermessage')
        return lockedusermessage
