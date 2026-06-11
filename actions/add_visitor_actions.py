from pages.add_visitor_front_officePages import AddVisitor
from actions.base_action import BaseAction
from utilities.logger import get_logger

logger = get_logger()
class AddvisiorActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.avp = AddVisitor()

    def clk_recpbtn(self):
        logger.info("Clicking Receptionist")
        self.click(self.avp.recpbtn)

    def clk_signin(self):
        logger.info("Clicking Sign In button")
        self.click(self.avp.signinbtn)

    def clck_frontofc(self):
        logger.info("Opening Front Office")
        self.click(self.avp.frontoffice)

        logger.info("Clicking Add Visitor")
        self.click(self.avp.addvisitorbtn)

    def add_inp(self, name, phone, idcard, noofperson, note):

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

    def clk_savebtn(self):
        logger.info("Clicking Save Button")
        self.click(self.avp.savebtn)

    def check_list(self):
        logger.info("Verifying Visitor List is displayed")
        status = self.is_displayed(self.avp.visitorlist)
        logger.info(f"Visitor List Displayed: {status}")
        return status
