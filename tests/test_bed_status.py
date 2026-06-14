import pytest
from actions.appointment_bed_status_action import bedstatusaction
from actions.login_action import LoginAction

@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class Testbedstatus:

    def test_bedstatus(self):

        bedsts = bedstatusaction(self.driver)
        baseact = LoginAction(self.driver)
        
        baseact.click_login("Receptionist")
        baseact.click_login_button()
        bedsts.clck_appointment()
        bedsts.clk_bedstatus()
        bedsts.clk_patient()
        assert bedsts.pateint_det_visible(), "Patient details are not displayed"
