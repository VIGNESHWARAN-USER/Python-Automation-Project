from pages.add_visitor_front_officePages import AddVisitor
from actions.base_action import BaseAction
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
from selenium.common.exceptions import StaleElementReferenceException
import pytest

logger = get_logger()

class AddvisiorActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.avp = AddVisitor()
        self.avsb = SideBarPage()

    def clk_recpbtn(self):
        try:
            logger.info("Clicking Receptionist")
            self.click(self.avp.recpbtn)

        except Exception as e:
            self.take_screenshot("receptionist_click_failure")
            pytest.fail(f"Unable to click Receptionist. Error: {str(e)}")

    def clk_signin(self):
        try:
            logger.info("Clicking Sign In button")
            self.click(self.avp.signinbtn)

        except Exception as e:
            self.take_screenshot("signin_click_failure")
            pytest.fail(f"Unable to click Sign In button. Error: {str(e)}")

    def clck_frontofc(self):
        try:
            logger.info("Opening Front Office")
            self.click(self.avsb.frontoffice)

            logger.info("Clicking Add Visitor")
            self.click(self.avp.addvisitorbtn)

        except Exception as e:
            self.take_screenshot("frontoffice_failure")
            pytest.fail(f"Unable to open Front Office/Add Visitor. Error: {str(e)}")

    def add_inp(self, name, phone, idcard, noofperson, note):
        try:
            logger.info("Selecting Purpose as Visit")
            self.select_by_text(self.avp.purpose, "Visit")
            logger.info(f"Entering Visitor Name: {name}")
            self.send_keys(self.avp.name, name)
            logger.info(f"Entering Phone: {phone}")
            self.send_keys(self.avp.phone, phone)
            logger.info(f"Entering ID Card: {idcard}")
            self.send_keys(self.avp.idcard, idcard)
            logger.info(f"Entering Number Of Persons: {noofperson}")
            self.send_keys(self.avp.noofperson, noofperson)
            logger.info(f"Entering Note: {note}")
            self.send_keys(self.avp.note, note)

        except Exception as e:
            self.take_screenshot("visitor_input_failure")
            pytest.fail(f"Unable to enter visitor details. Error: {str(e)}")

    def clk_savebtn(self):
        try:
            logger.info("Clicking Save Button")
            self.click(self.avp.savebtn)

        except Exception as e:
            self.take_screenshot("save_button_failure")
            pytest.fail(f"Unable to click Save Button. Error: {str(e)}")

    def check_list(self):
        try:
            logger.info("Verifying Visitor List is displayed")
            status = self.is_displayed(self.avp.visitorlist)
            logger.info(f"Visitor List Displayed: {status}")
            return status

        except StaleElementReferenceException:
            logger.warning("Stale element found while verifying visitor list. Retrying...")
            status = self.is_displayed(self.avp.visitorlist)
            logger.info(f"Visitor List Displayed After Retry: {status}")
            return status

        except Exception as e:
            self.take_screenshot("visitor_list_failure")
            pytest.fail(f"Visitor List verification failed. Error: {str(e)}")