import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--host", action="store", help="input either url or ip address")
    parser.addoption("--username", action="store", help="input username")
    parser.addoption("--password", action="store", help="input password")
    parser.addoption("--ip", action="store", help="input ip to search")
    parser.addoption("--headless", action="store", help="input in order to start headless session")


@pytest.fixture
def params(request):
    params = {}
    params['host'] = request.config.getoption('--host')
    params['username'] = request.config.getoption('--username')
    params['password'] = request.config.getoption('--password')
    params['ip'] = request.config.getoption('--ip')
    params['headless'] = request.config.getoption('--headless')
    return params


@pytest.fixture
def app():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

