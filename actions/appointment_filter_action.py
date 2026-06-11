from actions.base_action import BaseAction
from pages.appointment_filter_pages import Apponintmentfilter
from utilities.logger import get_logger

logger = get_logger()


class Appfilter(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.filter = Apponintmentfilter()

    def clk_appointment(self):
        logger.info("Clicking Appointment tab")
        self.click(self.filter.appointmentbtn)

    def check_todayapp(self):
        logger.info("Verifying Today Appointment table")
        status = self.is_displayed(self.filter.todayapptable)
        logger.info(f"Today Appointment table displayed: {status}")
        return status

    def clk_upcom_app(self):
        logger.info("Clicking Upcoming Appointment tab")
        self.click(self.filter.upcomingapp)

    def check_upcom_table(self):
        logger.info("Verifying Upcoming Appointment table")
        status = self.is_displayed(self.filter.upcomingapptable)
        logger.info(f"Upcoming Appointment table displayed: {status}")
        return status

    def clk_old_app(self):
        logger.info("Clicking Old Appointment tab")
        self.click(self.filter.oldapp)

    def check_old_table(self):
        logger.info("Verifying Old Appointment table")
        status = self.is_displayed(self.filter.oldapptable)
        logger.info(f"Old Appointment table displayed: {status}")
        return status