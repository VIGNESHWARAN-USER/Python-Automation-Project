import pytest
from actions.apply_leave_action import ApplyLeaveAction
from utilities.csvreader import get_data
from actions.login_action import LoginAction

@pytest.mark.mythily
@pytest.mark.usefixtures("setup_and_teardown")
class TestApplyLeave:
    
    @pytest.fixture(autouse=True)
    def setup(self, setup_and_teardown):
        self.al = ApplyLeaveAction(self.driver)
        self.la = LoginAction(self.driver)
        self.la.click_login("Pathologist")
        self.la.click_login_button()
        self.al.click_human_res()
        self.al.click_leaves_tab()
        self.al.click_apply_leave()

    @pytest.mark.parametrize("leavetype,reason", get_data("applyleavedata.csv"))
    def test_valid_applyleave(self, leavetype,reason):
        self.al.select_leave_type(leavetype)
        self.al.select_leave_from()
        self.al.select_leave_to()
        self.al.enter_reason(reason)
        self.al.click_save()
        self.al.get_success_message()

    @pytest.mark.parametrize("leavetype,reason", get_data("applyleavedata.csv"))
    def test_partial_applyleave(self, leavetype,reason):
        self.al.select_leave_type(leavetype)
        self.al.select_leave_from()
        self.al.enter_reason(reason)
        self.al.click_save()
        self.al.get_missing_field_message()

    def test_Invalid_applyleave(self):
        self.al.click_save()
        self.al.get_empty_field_message()