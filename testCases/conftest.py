# Necessary Imports for webDriver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture()
def setup(browser):  # Cross browser method which will accept input from command line
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox browser............")
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print("Launching Opera browser............")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching default browser Chrome browser.....")
    return driver


def pytest_addoption(parser):  # This will get value from command line
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return Browser value to setup method
    return request.config.getoption("--browser")


# PyTest HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Sauce Demo App Automation'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Monika'


# Hook for delete/Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
