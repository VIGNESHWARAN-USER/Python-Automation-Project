from actions.base_action import BaseAction
from pages.calllog_front_office_page import CallLogPage
from utilities.logger import get_logger
import pytest
from selenium.common.exceptions import StaleElementReferenceException
from pages.sidebar_page import SideBarPage
logger = get_logger()

class CallLogFrontofcActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cfp = CallLogPage()
        self.avsb = SideBarPage()

    def clckrecp(self):
        try:
            logger.info("clicking reception button")
            self.wait_for_visibility(self.cfp.recbtnfo)
            self.js_click(self.cfp.recbtnfo)

        except Exception as e:
            pytest.fail(f"Unable to click receptionist button. Error: {str(e)}")

    def clksign(self):
        try:
            logger.info("clicking sign in button")
            self.wait_for_visibility(self.cfp.signinfo)
            self.js_click(self.cfp.signinfo)

        except Exception as e:
            pytest.fail(f"Unable to click sign in button. Error: {str(e)}")

    def frontofclink(self):
        try:
            logger.info("clicking front office link")
            self.wait_for_visibility(self.cfp.frontofc)
            self.js_click(self.avsb.frontoffice)
            #self.js_click(self.cfp.frontofc)

        except Exception as e:
            pytest.fail(f"Unable to click front office link. Error: {str(e)}")

    def phcalllog(self):
        try:
            logger.info("clicking phone call log button")
            self.wait_for_visibility(self.cfp.phcalllog)
            self.js_click(self.cfp.phcalllog)

        except Exception as e:
            pytest.fail(f"Unable to click phone call log. Error: {str(e)}")

    def addcall(self):
        try:
            logger.info("clicking add call button")
            self.wait_for_visibility(self.cfp.addlog)
            self.js_click(self.cfp.addlog)

        except Exception as e:
            pytest.fail(f"Unable to click add call button. Error: {str(e)}")

    def enterdet(self, name, phone, description, calltype, note, duration):
        try:
            self.send_keys(self.cfp.name, name)
            self.send_keys(self.cfp.phone, phone)
            self.send_keys(self.cfp.desc, description)
            self.send_keys(self.cfp.note, note)
            self.send_keys(self.cfp.callduration, duration)

            if calltype.lower() == "incoming":
                self.js_click(self.cfp.incom)

            elif calltype.lower() == "outgoing":
                self.js_click(self.cfp.outgng)

        except Exception as e:
            pytest.fail(f"Unable to enter call details. Error: {str(e)}")

    def clicksave(self):
        try:
            logger.info("clicking save button")
            self.wait_for_visibility(self.cfp.savebtn)
            self.js_click(self.cfp.savebtn)

        except Exception as e:
            pytest.fail(f"Unable to click save button. Error: {str(e)}")

    def checklist(self):
            try:
                logger.info("checking whether list is visible")

                for _ in range(3):
                    try:
                        self.wait_for_visibility(self.cfp.checklist)
                        return self.get_text(self.cfp.checklist)

                    except StaleElementReferenceException:
                        logger.warning("Retrying due to stale element")

                pytest.fail("Checklist not visible after retries")

            except Exception as e:
                pytest.fail(f"Checklist not visible. Error: {str(e)}")

    def errorcheck(self):
        try:
            return self.is_displayed(self.cfp.error)

        except Exception:
            return False
