import pytest
from actions.appointment_filter_action import Appfilter
from actions.login_action import LoginAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class Testfilter:

    def test_appointmentfilter(self):

        log = LoginAction(self.driver)
        af = Appfilter(self.driver)

        log.click_login("Receptionist")
        log.click_login_button()

        af.clk_appointment()

        af.clk_today_app()
        assert af.check_todayapp(), "Today Appointment table is not displayed"

        af.clk_old_app()
        assert af.check_old_table(),"Old Appointment table is not displayed"

        af.clk_upcom_app()
        assert af.check_upcom_table(),"Upcoming Appointment table is not displayed"

    def test_appointment_page(self):

        log = LoginAction(self.driver)
        af = Appfilter(self.driver)

        log.click_login("Receptionist")
        log.click_login_button()

        assert af.appointment_visible(),"Appointment menu not displayed"