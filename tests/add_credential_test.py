import pytest
from utilities.config_reader import get_value
from utilities.excel_reader import get_data
from actions.join_consultation_action import JoinConsultationAction
from actions.login_action import LoginAction

@pytest.mark.vigneshwaran
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddCredentials:

    @pytest.fixture(autouse=True)   
    def setup(self, setup_and_teardown):
        self.ca = JoinConsultationAction(self.driver)
        self.la = LoginAction(self.driver)
        self.la.click_login("Doctor")
        self.la.click_login_button()
        self.ca.click_live_consultation_dropdown()
        self.ca.click_live_consultation_option()
        self.ca.click_add_credential_button()

    def test__with_valid_credentials(self):
        self.ca.clear_credential_fields()
        self.ca.enter_zoom_api_key(get_value("./data_files/consultation_data.ini", "data set", "key"))
        self.ca.enter_zoom_api_secret(get_value("./data_files/consultation_data.ini", "data set", "secret"))
        self.ca.click_save_credential_button()
        assert self.ca.is_credentials_added(), "Cannot add credentials"

    @pytest.mark.xfail()
    @pytest.mark.parametrize("test,key,secret",get_data("credentials_data.xlsx", "InvalidDataSet"))
    def test_with_invalid_credentials(self, test, key, secret):
        self.ca.enter_zoom_api_key(key)
        self.ca.enter_zoom_api_secret(secret)
        self.ca.click_save_credential_button()

        actual_message = self.ca.get_toast_message()

        assert actual_message.strip(), "Toast message is empty"

        assert "Error" in actual_message, (
            f"Validation message mismatch. Actual: {actual_message}"
        )

    