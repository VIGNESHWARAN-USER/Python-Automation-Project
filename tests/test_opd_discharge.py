# tests/test_opd_discharge.py
# Feature  : Jerishwin_Joseph_25-05-2026_Discharge Patient
# Author   : Jerishwin Joseph
# Tags     : @OpdDischarge @jerishwin @UnderDevelopment
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
        # Background: Given the user is logged into the Smart Hospital portal as a receptionist
        self._login()

        action = OPDDischargeAction(self.driver)

        # Background: And the user is on the OPD page
        action.navigate_to_opd_page()

        # When: the user clicks the ID link for that patient
        logger.info("Step: Clicking patient ID link / navigating to OPD")
        action.click_patient_id_link()

        # And: clicks on the Discharge icon
        logger.info("Step: Clicking discharge icon")
        action.click_discharge_icon()

        # And: fills in the discharge form and clicks the Save button
        logger.info("Step: Filling discharge form")
        action.fill_discharge_form()
        logger.info("Step: Clicking Save button")
        action.click_save_discharge_button()

        # Then: a Record Saved Successfully message should appear
        logger.info("Step: Verifying success message")
        assert action.is_success_message_displayed(), \
            "Expected 'Record Saved Successfully' message was not displayed after discharge"