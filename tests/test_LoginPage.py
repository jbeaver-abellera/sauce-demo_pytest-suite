import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from conftest import suite_conftest

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    yield loginPage

    # '''Teardown'''
    # dropdownPage.navigateToHome()
    
# @pytest.mark.parametrize('username', ['standard_user', 'locked_out_user'])
def test_login(setup_teardown):
    loginPage = setup_teardown
    username = 'standard_user'
    password = 'secret_sauce'
    initial_url = loginPage.driver.current_url
    loginPage.login(username, password)
    try:
        loginPage.driver = WebDriverWait(loginPage.driver, 30).until(lambda driver: loginPage.driver.current_url != initial_url)
    except TimeoutException:
        raise AssertionError(f'Timeout error. Checkbox did not toggle.')