from actions.base_action import BaseAction
from pages.apply_leave_page import ApplyLeavePage
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger

logger = get_logger()

class ApplyLeaveAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.al = ApplyLeavePage()
        self.sp = SideBarPage()

    def click_human_res(self):
        try:
            self.click(self.sp.humanRes)
            logger.info("Successfully clicked Human Resource menu")
        except Exception as e:
            logger.error(f"failed to click human resourse on sidebar manu: {str(e)}")

    def click_leaves_tab(self):
        try:
            self.click(self.al.leaves)
            logger.info("Successfully clicked Leaves tab")
        except Exception as e:
            logger.error(f"failed to click leaves tab: {str(e)}")

    def click_apply_leave(self):
        try:
            self.click(self.al.applyLeave)
            logger.info("Successfully clicked Apply Leave button")
        except Exception as e:
            logger.error(f"failed to click apply leave button: {str(e)}")

    def select_leave_type(self):
        try:
            self.select_by_text(self.al.leaveType)
            logger.info("Successfully selected Leave Type")
        except Exception as e:
            logger.error(f"failed to select leave type: {str(e)}")

    def select_leave_from(self):
        try:
            self.select_by_text(self.al.leaveFrom)
            logger.info("Successfully selected Leave From date")
        except Exception as e:
            logger.error(f"failed to select leave from: {str(e)}")

    def select_leave_to(self):
        try:
            self.select_by_text(self.al.leaveTo)
            logger.info("Successfully selected Leave To date")
        except Exception as e:
            logger.error(f"failed to select leave to: {str(e)}")

    def enter_reason(self):
        try:
            self.send_keys(self.al.reason)
            logger.info("Successfully entered leave reason")
        except Exception as e:
            logger.error(f"failed to enter the reason: {str(e)}")

    def click_save(self):
        try:
            self.click(self.al.savebtn)
            logger.info("Successfully clicked Save button")
        except Exception as e:
            logger.error(f"failed to click save button: {str(e)}")    