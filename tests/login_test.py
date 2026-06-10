import pytest
from utilities.excel_reader import get_data

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("role", get_data("login_data.xlsx", "ValidLogindata"))
    def test_valid_login_test(self, role):
        pass

    @pytest.mark.parametrize("email,password,message", get_data("login_data.xlsx", "InvalidLoginData"))
    def test_login_with_invalid_email_or_password(self, email, password,message):
        pass

    def test_login_with_empty_email(self):
        pass

    def test_login_with_empty_password(self):
        pass

    def test_login_with_empty_email_and_password(self):
        pass

    
