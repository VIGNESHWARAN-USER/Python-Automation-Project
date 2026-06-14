import logging
import pytest
from actions.opd_discharge_action import OPDDischargeAction
from actions.login_action import LoginAction
logger = logging.getLogger(__name__)

@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestOPDDischarge:

    def _login(self):
        login = LoginAction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()

    def test_discharge_patient_and_verify_success_message(self):
        self._login()

        action = OPDDischargeAction(self.driver)

        action.navigate_to_opd_page()

        logger.info("Step: Clicking patient ID link / navigating to OPD")
        action.click_patient_id_link()

        logger.info("Step: Clicking discharge icon")
        action.click_discharge_icon()

        logger.info("Step: Filling discharge form")
        action.fill_discharge_form()
        logger.info("Step: Clicking Save button")
        action.click_save_discharge_button()

        logger.info("Step: Verifying success message")
        assert action.is_success_message_displayed(), \
            "Expected 'Record Saved Successfully' message was not displayed after discharge"