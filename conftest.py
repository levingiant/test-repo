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


@pytest.fixture(autouse=True)
def app():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-gpu")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument("no-sandbox")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

