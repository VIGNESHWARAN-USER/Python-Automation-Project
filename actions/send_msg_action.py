from actions.base_action import BaseAction
from pages.sendmsg_page import SendMsg
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger

logger = get_logger()

class SendMsgAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.sm = SendMsg()
        self.sp = SideBarPage()

    def click_msg(self):
        try:
            self.click(self.sp.messaging)
            logger.info("Clicked Messaging menu successfully")
        except Exception as e:
            logger.error(f"failed to click the messaging menu: {str(e)}")

    def click_sendSMS(self):
        try:
            self.click(self.sm.sendSms)
            logger.info("Clicked Messaging menu successfully")
        except Exception as e:
            logger.error(f"failed to click the send sms: {str(e)}")

    def enter_title(self,title):
        try:
            self.send_keys(self.sm.title,title)
            logger.info(f"Entered title: {title}")
        except Exception as e:
            logger.error(f"failed to enter titel: {str(e)}")

    def enter_tempid(self, tempid):
        try:
            self.send_keys(self.sm.tempId,tempid)
            logger.info(f"Entered template ID: {tempid}")
        except Exception as e:
            logger.error(f"failed to enter template id: {str(e)}")

    def click_sendthrough(self):
        try:
            self.click(self.sm.sms , self.sm.sms)
            logger.info("Selected SMS as send through option")
        except Exception as e:
            logger.error(f"failed to click the send through: {str(e)}")
    
    def enter_msg(self, msg):
        try:
            self.send_keys(self.sm.message,msg)
            logger.info("Entered SMS message successfully")
        except Exception as e:
            logger.error(f"failed to enter message: {str(e)}")

    def select_msgto(self):
        try:
            self.select_by_text(self.sm.dtr , self.sm.nurse)
            logger.info("Selected Nurse from Message To dropdown")
        except Exception as e:
            logger.error(f"failed to select the message to: {str(e)}")        
    
    def click_send(self):
        try:
            self.click(self.sm.send)
            logger.info("Clicked Send button successfully")
        except Exception as e:
            logger.error(f"failed to send the SMS: {str(e)}")    

    def get_success_msg(self):
        try:
            status = self.is_displayed(self.sm.success_msg)
            logger.info("Success message displayed")
            return status
        except Exception as e:
            logger.error(f"failed to displayed success msg: {str(e)}")

    def get_error_msg(self):
        try:
            status = self.is_displayed(self.sm.error_msg)
            logger.info("Error message displayed")
            return status
        except Exception as e:
            logger.error(f"failed to handle error msg: {str(e)}") 

    def get_missing_field_msg(self):
        try:
            status = self.is_displayed(self.sm.missing_field_msg)
            logger.info("Missing field validation message displayed")
            return status
        except Exception as e:
            logger.error(f"failed to handle missing field error msg: {str(e)}")                                          