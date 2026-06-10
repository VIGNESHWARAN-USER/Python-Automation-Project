import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.excel_reader import get_data
from utilities.logger import get_logger
from actions.login_action import LoginAction

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.order(2)
    @pytest.mark.parametrize("email,password",get_data("login_data.xlsx", "ValidLoginData"))
    def test_valid_login(self, email, password):
        logger = get_logger()
        self.la = LoginAction(self.driver)
        
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))

        self.la.login(email, password)
        
        
        logger.info("Login Successful")


    @pytest.mark.order(1)
    @pytest.mark.parametrize("email,password,message",get_data("login_data.xlsx", "InvalidLoginData"))
    def test_invalid_login(self, email, password, message):
        logger = get_logger()
        self.la = LoginAction(self.driver)
        
        self.driver.save_screenshot("homepage.png")
        print("Current URL:", self.driver.current_url)
        print("Title:", self.driver.title)
        print("Page Source Length:", len(self.driver.page_source))

        self.la.login(email, password)

        assert self.la.check_error_message(message)
        logger.info("Error message shown Successful")
