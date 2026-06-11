from pages.add_visitor_front_officePages import AddVisitor
from actions.base_action import BaseAction


class AddvisiorActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.avp = AddVisitor()

        
    def clk_recpbtn(self):
        self.click(self.avp.recpbtn)

    def clk_signin(self):
        self.click(self.avp.signinbtn)
        
    

    def clck_frontofc(self):
        self.click(self.avp.frontoffice)
        self.click(self.avp.addvisitorbtn)

    def add_inp(self, name, phone, idcard, noofperson, note):

        self.select_by_text(self.avp.purpose, "Visit")

        self.send_keys(self.avp.name, name)
        self.send_keys(self.avp.phone, phone)
        self.send_keys(self.avp.idcard, idcard)
        self.send_keys(self.avp.noofperson, noofperson)
        self.send_keys(self.avp.note, note)

    def clk_savebtn(self):
        self.click(self.avp.savebtn)

    def check_list(self):
        return self.is_displayed(self.avp.visitorlist)