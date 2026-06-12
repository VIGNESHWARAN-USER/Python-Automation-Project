from actions.base_action import BaseAction
from pages.leavemsg_page import LeaveMsg
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger

logger = get_logger()

class PathalogyAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.lm = LeaveMsg()
        self.sp = SideBarPage()

    def click_pathologist_login(self):
        try:
            self.click(self.lm.pathologistBtn)
        except Exception as e:
            logger.error(f"failed to login to the pathologist: {str(e)}")        

    def click_signin(self):
        try:
           self.click(self.lm.signInBtn)
        except Exception as e:
            logger.error(f"failed to signup to pathologist: {str(e)}")

    def click_msg(self):
        try:
            self.click(self.sp.messaging)
        except Exception as e:
            logger.error(f"failed to click the messaging menu: {str(e)}")

    def click_sendSMS(self):
        try:
            self.click(self.lm.sendSms)
        except Exception as e:
            logger.error(f"failed to click the send sms: {str(e)}")

    def enter_title(self,title):
        try:
            self.send_keys(self.lm.title,title)
        except Exception as e:
            logger.error(f"failed to enter titel: {str(e)}")

    def enter_tempid(self, tempid):
        try:
            self.send_keys(self.lm.tempId,tempid)
        except Exception as e:
            logger.error(f"failed to enter template id: {str(e)}")

    def click_sendthrough(self):
        try:
            self.click(self.lm.sms , self.lm.sms)
        except Exception as e:
            logger.error(f"failed to click the send through: {str(e)}")

    def click_send(self):
        try:
            self.click(self.lm.send)
        except Exception as e:
            logger.error(f"failed to send the SMS: {str(e)}")

    def get_success_msg(self):
        try:
            return self.is_displayed(self.get_success_msg())
        except Exception as e:
            logger.error(f"failed to displayed success msg: {str(e)}")

    def get_error_msg(self):
        try:
            return self.is_displayed(self.get_error_msg())
        except Exception as e:
            logger.error(f"failed to handle error msg: {str(e)}") 

    def get_missing_field_msg(self):
        try:
            return self.is_displayed(self.get_missing_field_msg())
        except Exception as e:
            logger.error(f"failed to handle missing field error msg: {str(e)}")                                          