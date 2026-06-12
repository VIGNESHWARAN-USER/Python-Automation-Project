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

    def click_pathologist_login(self):
        try:
            self.click(self.sm.pathologistBtn)
        except Exception as e:
            logger.error(f"failed to login to the pathologist: {str(e)}")        

    def click_signin(self):
        try:
           self.click(self.sm.signInBtn)
        except Exception as e:
            logger.error(f"failed to signup to pathologist: {str(e)}")

    def click_msg(self):
        try:
            self.click(self.sp.messaging)
        except Exception as e:
            logger.error(f"failed to click the messaging menu: {str(e)}")

    def click_sendSMS(self):
        try:
            self.click(self.sm.sendSms)
        except Exception as e:
            logger.error(f"failed to click the send sms: {str(e)}")

    def enter_title(self,title):
        try:
            self.send_keys(self.sm.title,title)
        except Exception as e:
            logger.error(f"failed to enter titel: {str(e)}")

    def enter_tempid(self, tempid):
        try:
            self.send_keys(self.sm.tempId,tempid)
        except Exception as e:
            logger.error(f"failed to enter template id: {str(e)}")

    def click_sendthrough(self):
        try:
            self.click(self.sm.sms , self.sm.sms)
        except Exception as e:
            logger.error(f"failed to click the send through: {str(e)}")
    
    def enter_msg(self, msg):
        try:
            self.send_keys(self.sm.message,msg)
        except Exception as e:
            logger.error(f"failed to enter message: {str(e)}")

    def select_msgto(self):
        try:
            self.select_by_text(self.sm.dtr , self.sm.nurse)
        except Exception as e:
            logger.error(f"failed to select the message to: {str(e)}")        
    
    def click_send(self):
        try:
            self.click(self.sm.send)
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