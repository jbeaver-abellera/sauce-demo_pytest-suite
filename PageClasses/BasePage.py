import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self):
        self.driver = utils.WebDriverSingleton.get_driver(isHeadless=False)
        
    def navigateToHome(self):
        self.driver.get(utils.Constants.WEBSITE_URL)
    