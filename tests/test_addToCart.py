import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from conftest import suite_conftest
import utils


@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    print('loginpage instantiated')
    loginPage.login(utils.Constants.USERNAME, utils.Constants.PASSWORD)
    inventoryPage = pc.InventoryPage(loginPage.driver)
    yield inventoryPage
    
    '''Teardown'''
    # dropdownPage.navigateToHome()
    
# @pytest.mark.parametrize('username', ['standard_user', 'locked_out_user'])
def test_addToCart(setup_teardown):
    inventoryPage = setup_teardown
    inventoryPage.sortItemsBy('Price (low to high)')
    itemsWebElementList = inventoryPage.itemsWebElementList
    for i in range(2):
        inventoryPage.addToCartItem(0)
    assert inventoryPage.shoppingCartBadge == '2'