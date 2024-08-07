import pytest
from selenium import webdriver

from configuration import ConfigProvider
from page.LoginPage import LoginPage
from test_data.DataProvieder import DataProvider
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture(scope='session')
def config():
    return ConfigProvider('test_config.ini')


@pytest.fixture(scope='session')
def test_data_login(config: ConfigProvider):
    filename = config.get('test_data', 'filename')
    provider = DataProvider(filename)
    return {'user': provider.get('user'), 'password': provider.get('password')}


@pytest.fixture
def driver(config: ConfigProvider):
    driver = webdriver.Chrome()
    driver.timeouts.implicit_wait = config.get_int('ui', 'timeout_seconds')
    #driver.timeouts.implicit_wait = 4
    yield driver
    if (driver != None):
        driver.quit()


@pytest.fixture
def login_page(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    page = LoginPage(driver)
    yield page

    driver.quit()


@pytest.fixture(scope='session')
def test_data_login():
    provider = DataProvider('test_data.json')
    return {'user': provider.get('user'), 'password': provider.get('password')}
