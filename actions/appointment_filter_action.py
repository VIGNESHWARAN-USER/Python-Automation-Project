from actions.base_action import BaseAction
from pages.appointment_filter_pages import Apponintmentfilter
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
import pytest

logger = get_logger()
class Appfilter(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.filter = Apponintmentfilter()
        self.avsb = SideBarPage()

    def clk_appointment(self):
        try:
            logger.info("Clicking Appointment tab")
            self.click(self.filter.appointmentbtn)

        except Exception as e:
            self.take_screenshot("appointment_tab_failure")
            pytest.fail(f"Unable to click Appointment tab. Error: {str(e)}")

    def clk_today_app(self):
        try:
            logger.info("Clicking Today Appointment tab")
            self.click(self.filter.todayapp)

        except Exception as e:
            self.take_screenshot("today_appointment_tab_failure")
            pytest.fail(f"Unable to click Today Appointment tab. Error: {str(e)}")

    def check_todayapp(self):
        try:
            logger.info("Verifying Today Appointment table")
            status = self.is_displayed(self.filter.todayapptable)
            logger.info(f"Today Appointment table displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("today_appointment_table_failure")
            pytest.fail(f"Today Appointment table verification failed. Error: {str(e)}")

    def clk_upcom_app(self):
        try:
            logger.info("Clicking Upcoming Appointment tab")
            self.click(self.filter.upcomingapp)

        except Exception as e:
            self.take_screenshot("upcoming_appointment_tab_failure")
            pytest.fail(f"Unable to click Upcoming Appointment tab. Error: {str(e)}")

    def check_upcom_table(self):
        try:
            logger.info("Verifying Upcoming Appointment table")
            status = self.is_displayed(self.filter.upcomingapptable)
            logger.info(f"Upcoming Appointment table displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("upcoming_appointment_table_failure")
            pytest.fail(f"Upcoming Appointment table verification failed. Error: {str(e)}")

    def clk_old_app(self):
        try:
            logger.info("Clicking Old Appointment tab")
            self.click(self.filter.oldapp)

        except Exception as e:
            self.take_screenshot("old_appointment_tab_failure")
            pytest.fail(f"Unable to click Old Appointment tab. Error: {str(e)}")

    def check_old_table(self):
        try:
            logger.info("Verifying Old Appointment table")
            status = self.is_displayed(self.filter.oldapptable)
            logger.info(f"Old Appointment table displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("old_appointment_table_failure")
            pytest.fail(f"Old Appointment table verification failed. Error: {str(e)}")
            
    def appointment_visible(self):
        try:
            logger.info("Checking Appointment Menu")
            status = self.is_displayed(self.filter.appointmentbtn)
            logger.info(f"Appointment Menu displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("appointment_visible_failure")
            pytest.fail(f"Appointment menu verification failed. Error: {str(e)}")