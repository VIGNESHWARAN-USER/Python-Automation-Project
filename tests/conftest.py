from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from utilities.config_reader import get_value


@pytest.fixture()
def setup_teardown(request):
    browser = get_value("config.ini", "basic info", "browser")
    if browser == "chrome":
        options = Options()
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
                "autofill.profile_enabled": False,
                "autofill.credit_card_enabled": False,
            },
        )

        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-features=AutofillServerCommunication")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--guest")
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(get_value("config.ini", "basic info", "url"))

    request.cls.driver = driver

    yield

    driver.quit()
