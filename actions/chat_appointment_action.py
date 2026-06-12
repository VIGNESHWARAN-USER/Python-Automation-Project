from actions.base_action import BaseAction
from pages.chat_appointment_pages import Chatpage
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
logger = get_logger()
class Chataction(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.cap = Chatpage()
        self.avsb = SideBarPage()
    
    def clickrecp(self):
        logger.info("clicking receptionist")
        self.click(self.cap.recbtn)

    def clicksignin(self):
        logger.info("clicking signin")
        self.click(self.cap.signin)

    def clickappointment(self):
        logger.info("clicking appointment section")
        self.click(self.avsb.appointmentbtn)
        #self.click(self.cap.appbtn)

    def clickchaticon(self):
        logger.info("clicking chat icon")
        self.click(self.cap.chatbtn)

    def selectdoctor(self):
        logger.info("selecting doctor")
        self.click(self.cap.person)

    def sendmessage(self):
        logger.info("sending message")
        self.send_keys(self.cap.msg,"Hello Doctor")
        self.click(self.cap.sendmsg)

    def verifymessage(self):
        logger.info("verifying message")
        return self.is_displayed(self.cap.check)