from pages.appointment_bed_status_pages import Bedstatus
from actions.base_action import BaseAction

class bedstatusaction(BaseAction):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.bsts = Bedstatus()
        
    def clck_appointment(self):
        self.click(self.bsts.appointmentbtn)
    def clk_bedstatus(self):
        self.click(self.bsts.bedlogo)
    def clk_patient(self):
        self.click(self.bsts.patient)
    def pateint_det_visible(self):
        return self.is_displayed(self.bsts.patientdetails)
    