from pages.appointment_bed_status_pages import Bedstatus
from actions.base_action import BaseAction
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
import pytest

logger = get_logger()


class bedstatusaction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.bsts = Bedstatus()
        self.avsb = SideBarPage()

    def clck_appointment(self):
        try:
            logger.info("Clicking Appointment menu")
            self.click(self.avsb.appointmentbtn)

        except Exception as e:
            self.take_screenshot("appointment_click_failure")
            pytest.fail(f"Unable to click Appointment menu. Error: {str(e)}")

    def clk_bedstatus(self):
        try:
            logger.info("Clicking Bed Status icon")
            self.click(self.bsts.bedlogo)

        except Exception as e:
            self.take_screenshot("bedstatus_click_failure")
            pytest.fail(f"Unable to click Bed Status icon. Error: {str(e)}")

    def clk_patient(self):
        try:
            logger.info("Clicking occupied patient bed")
            self.click(self.bsts.patient)

        except Exception as e:
            self.take_screenshot("patient_click_failure")
            pytest.fail(f"Unable to click patient bed. Error: {str(e)}")

    def pateint_det_visible(self):
        try:
            logger.info("Verifying patient details popup/page")
            status = self.is_displayed(self.bsts.patientdetails)
            logger.info(f"Patient details displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("patient_details_failure")
            pytest.fail(f"Patient details verification failed. Error: {str(e)}")