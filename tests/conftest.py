import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.config_reader import get_value


@pytest.fixture()
def setup_and_teardown(request):

    browser = get_value("./configurations/config.ini","basic info","browser")

    if browser == "chrome":

        options = Options()

        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--remote-allow-origins=*")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-password-generation")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        download_path = os.path.join(os.getcwd(), "downloads")

        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "safebrowsing.enabled": True
        }

        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(
        get_value(
            "./configurations/config.ini",
            "basic info",
            "url"
        )
    )

    request.cls.driver = driver

    yield

    driver.quit()