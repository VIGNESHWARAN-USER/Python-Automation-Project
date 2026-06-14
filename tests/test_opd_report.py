# tests/test_opd_report.py
import logging
import pytest
from actions.login_action import LoginAction
from actions.opd_report_action import OPDReportAction

logger = logging.getLogger(__name__)

@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestOPDReport:

    def _login(self):
        login = LoginAction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
    

    def test_report_download_successfully(self):
        self._login()

        action = OPDReportAction(self.driver)

        action.navigate_to_opd_out_patient_page()

        logger.info("Step: Clicking ID link / Show icon")
        action.click_show_icon()

        logger.info("Step: Clicking Visits tab")
        action.click_visits_tab()

        logger.info("Step: Clicking PDF / Print icon")
        action.click_print_icon()

        logger.info("Step: Verifying report download")
        assert action.is_report_downloaded_successfully(), \
            "Report did not open/download successfully."