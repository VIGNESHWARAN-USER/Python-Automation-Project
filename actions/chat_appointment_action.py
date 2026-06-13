from actions.base_action import BaseAction
from pages.chat_appointment_pages import Chatpage
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
import pytest

logger = get_logger()


class Chataction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cap = Chatpage()
        self.avsb = SideBarPage()

    def clickrecp(self):
        try:
            logger.info("clicking receptionist")
            self.click(self.cap.recbtn)

        except Exception as e:
            self.take_screenshot("chat_receptionist_failure")
            pytest.fail(f"Unable to click receptionist. Error: {str(e)}")

    def clicksignin(self):
        try:
            logger.info("clicking signin")
            self.click(self.cap.signin)

        except Exception as e:
            self.take_screenshot("chat_signin_failure")
            pytest.fail(f"Unable to click signin. Error: {str(e)}")

    def clickappointment(self):
        try:
            logger.info("clicking appointment section")
            self.click(self.avsb.appointmentbtn)

        except Exception as e:
            self.take_screenshot("chat_appointment_failure")
            pytest.fail(f"Unable to click appointment section. Error: {str(e)}")

    def clickchaticon(self):
        try:
            logger.info("clicking chat icon")
            self.click(self.cap.chatbtn)

        except Exception as e:
            self.take_screenshot("chat_icon_failure")
            pytest.fail(f"Unable to click chat icon. Error: {str(e)}")

    def selectdoctor(self):
        try:
            logger.info("selecting doctor")
            self.click(self.cap.person)

        except Exception as e:
            self.take_screenshot("chat_doctor_failure")
            pytest.fail(f"Unable to select doctor. Error: {str(e)}")

    def sendmessage(self):
        try:
            logger.info("sending message")
            self.send_keys(self.cap.msg, "Hello Doctor")
            self.click(self.cap.sendmsg)

        except Exception as e:
            self.take_screenshot("chat_sendmessage_failure")
            pytest.fail(f"Unable to send message. Error: {str(e)}")

    def verifymessage(self):
        try:
            logger.info("verifying message")

            status = self.is_displayed(self.cap.check)

            logger.info(f"Message displayed: {status}")

            return status

        except Exception as e:
            self.take_screenshot("chat_verify_failure")
            pytest.fail(f"Message verification failed. Error: {str(e)}")
    def verifydoctorlist(self):
        try:
            logger.info("Verifying doctor list")
            status = self.is_displayed(self.cap.person)
            logger.info(f"Doctor list displayed: {status}")
            return status

        except Exception as e:
            self.take_screenshot("doctor_list_failure")
            pytest.fail(f"Doctor list verification failed. Error: {str(e)}")