import pytest
from actions.login_action import LoginAction
from actions.OPD_Search_Action import OPDSearchActions

@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestOPDSearch:

    def test_search_existing_patient(self):
        login = LoginAction(self.driver)
        opd = OPDSearchActions(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        opd.navigate_to_opd_page()
        opd.search_patient("Maria")
        actual_name = opd.verify_search_name_result()
        print(f"Patient Name Found: {actual_name}")
        assert "Maria" in actual_name, \
            f"Expected patient name to contain 'Maria', but got '{actual_name}'"

    def test_search_non_existing_patient(self):
        login = LoginAction(self.driver)
        opd = OPDSearchActions(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        opd.navigate_to_opd_page()
        opd.search_patient("XYZ123")
        actual_message = opd.verify_search_failed()
        print(f"Message Displayed: {actual_message}")
        assert "No data available in table" in actual_message, \
            f"Expected 'No data available in table', but got '{actual_message}'"