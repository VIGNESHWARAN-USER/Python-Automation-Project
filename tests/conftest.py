import pytest
from selenium import webdriver
from utilities.config_reader import get_value


@pytest.fixture()
def setup_teardown(request):

    browser = get_value("config.ini","basic info", "browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(get_value("config.ini","basic info", "url"))

    request.cls.driver = driver

    yield

    driver.quit()
