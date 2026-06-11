from actions.base_action import BaseAction
from pages.complaint_front_office import ComplaintFoPages
from utilities.logger import get_logger
import pytest
from datetime import datetime
logger = get_logger()


class ComplaintActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cp = ComplaintFoPages()

    def clickrescp(self):
        try:
            logger.info("clicking reception button")
            self.click(self.cp.recbtnfo)

            logger.info("clicking signin button")
            self.click(self.cp.signinfo)

        except Exception as e:
            pytest.fail(f"Unable to click receptionist/signin button. Error: {str(e)}")

    def clkfo(self):
        try:
            logger.info("clicking front office button")
            self.click(self.cp.frontofc)

        except Exception as e:
            pytest.fail(f"Unable to click front office button. Error: {str(e)}")

    def clkcom(self):
        try:
            logger.info("clicking complaint button")
            self.click(self.cp.complaint)

        except Exception as e:
            pytest.fail(f"Unable to click complaint button. Error: {str(e)}")

    def addcomp(self):
        try:
            logger.info("clicking add complaint button")
            self.click(self.cp.addcomp)

        except Exception as e:
            pytest.fail(f"Unable to click add complaint button. Error: {str(e)}")

    def compdet(self,complainttype,source,complainby,phone,date,description,actiontaken,assigned,note,):
        try:
            logger.info(f"Selecting Complaint Type: {complainttype}")
            self.select_by_text(self.cp.comtype, complainttype)

            logger.info(f"Selecting Source: {source}")
            self.select_by_text(self.cp.src, source)

            logger.info(f"Entering Complain By: {complainby}")
            self.send_keys(self.cp.complainby, complainby)

            logger.info(f"Entering Phone: {phone}")
            self.send_keys(self.cp.phone, phone)

            logger.info(f"Entering Date: {date}")
            self.send_keys(self.cp.date,date.strftime("%d/%m/%Y"))

            logger.info("Entering Description")
            self.send_keys(self.cp.desc, description)

            logger.info("Entering Action Taken")
            self.send_keys(self.cp.actiontaken, actiontaken)

            logger.info("Entering Assigned")
            self.send_keys(self.cp.assigned, assigned)

            logger.info("Entering Note")
            self.send_keys(self.cp.note, note)

        except Exception as e:
            pytest.fail(f"Unable to enter complaint details. Error: {str(e)}")

    def savebtn(self):
        try:
            logger.info("clicking save button")
            self.click(self.cp.savebtn)

        except Exception as e:
            pytest.fail(f"Unable to click save button. Error: {str(e)}")

    def checklistcom(self):
        try:
            logger.info("checking complaint list")

            status = self.get_text(self.cp.checklistcomp)

            logger.info(f"Complaint List Text: {status}")

            return status

        except Exception as e:
            pytest.fail(f"Complaint list not visible. Error: {str(e)}")

    def emptyfields(self):
        try:
            logger.info("checking whether required field validation is displayed")

            status = self.is_displayed(self.cp.emptyfields)

            logger.info(f"Required Field Validation Displayed: {status}")

            return status

        except Exception:
            return False
