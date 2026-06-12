import pytest
from utilities.excel_reader import get_data
from actions.login_action import LoginAction
from utilities.config_reader import get_value

@pytest.mark.vigneshwaran
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
        
    @pytest.mark.parametrize("role", get_data("login_data.xlsx", "ValidLoginData"))
    def test_valid_login_test(self, role):
        self.la = LoginAction(self.driver)
        self.la.click_login(role[0])
        self.la.click_login_button()
        assert self.la.is_correct_user_logged_in(role[0])

    @pytest.mark.parametrize("email,password,message", get_data("login_data.xlsx", "InvalidLoginData"))
    def test_login_with_invalid_email_or_password(self, email, password,message):
        self.la = LoginAction(self.driver)
        self.la.set_username(email)
        self.la.set_password(password)
        self.la.click_login_button()
        assert self.la.is_correct_error_message_displayed(message)

    def test_login_with_empty_email(self):
        self.la = LoginAction(self.driver)
        self.la.set_username("")
        self.la.set_password(get_value("./data_files/sample_login_data.ini", "credentials", "password"))
        self.la.click_login_button()
        message = get_value("./data_files/sample_login_data.ini", "error message", "username_error_message")
        assert self.la.is_username_error_message_displayed(message)

    def test_login_with_empty_password(self):
        self.la = LoginAction(self.driver)
        self.la.set_username(get_value("./data_files/sample_login_data.ini", "credentials", "email"))
        self.la.set_password("")
        self.la.click_login_button()
        message = get_value("./data_files/sample_login_data.ini", "error message", "password_error_message")
        assert self.la.is_password_error_message_displayed(message)

    def test_login_with_empty_email_and_password(self):
        self.la = LoginAction(self.driver)
        self.la.set_username("")
        self.la.set_password("")
        self.la.click_login_button()
        messages = [get_value("./data_files/sample_login_data.ini", "error message", "password_error_message"),
                   get_value("./data_files/sample_login_data.ini", "error message", "username_error_message")]
        assert self.la.is_validation_error_messages_displayed(messages)

    
