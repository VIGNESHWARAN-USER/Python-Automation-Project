import pytest
from actions.add_visitor_actions import AddvisiorActions
from utilities import csvreader
from actions.login_action import LoginAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddVisitor:

    @pytest.mark.parametrize("name,phone,idcard,noofperson,note",csvreader.get_data("addvisitordata.csv"))
    def test_addvisitors(self, name, phone, idcard, noofperson, note):

        la = LoginAction(self.driver)
        adv = AddvisiorActions(self.driver)
        la.click_login("Receptionist")
        la.click_login_button()
        adv.clck_frontofc()
        adv.add_inp(name, phone, idcard, noofperson, note)
        adv.clk_savebtn()

        assert adv.check_list(),f"Visitor List is not displayed after adding visitor: {name}"

    def test_addvisitor_page_open(self):

        la = LoginAction(self.driver)
        adv = AddvisiorActions(self.driver)
        la.click_login("Receptionist")
        la.click_login_button()
        adv.clck_frontofc()
        assert adv.is_displayed(adv.avp.name), "Add Visitor form is not displayed"