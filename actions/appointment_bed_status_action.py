from pages.appointment_bed_status_pages import Bedstatus
from actions.base_action import BaseAction
from utilities.logger import get_logger

logger = get_logger()
class bedstatusaction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.bsts = Bedstatus()

    def clck_appointment(self):
        logger.info("Clicking Appointment menu")
        self.click(self.bsts.appointmentbtn)

    def clk_bedstatus(self):
        logger.info("Clicking Bed Status icon")
        self.click(self.bsts.bedlogo)

    def clk_patient(self):
        logger.info("Clicking occupied patient bed")
        self.click(self.bsts.patient)

    def pateint_det_visible(self):
        logger.info("Verifying patient details popup/page")
        status = self.is_displayed(self.bsts.patientdetails)
        logger.info(f"Patient details displayed: {status}")
        return status
