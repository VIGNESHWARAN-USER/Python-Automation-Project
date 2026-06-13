import pytest
from actions.send_msg_action import SendMsgAction
from actions.login_action import LoginAction
from utilities.excel_reader import get_data

@pytest.mark.usefixtures("setup_and_teardown")
class TestSendMsg:
    
    @pytest.fixture(autouse=True)
    def setup(self, setup_and_teardown):
        self.sm = SendMsgAction(self.driver)
        self.la = LoginAction(self.driver)
        self.la.click_login("Pathologist")
        self.la.click_login_button()
        self.sm.click_msg()
        self.sm.click_sendSMS()

    @pytest.mark.parametrize("title,tempId,msg", get_data("SendMsgData.xlsx", "ValidMsg"))
    def test_valid_msg(self, title,tempId,msg):
        self.sm = SendMsgAction(self.driver)
        self.sm.enter_title(title)
        self.sm.enter_tempid(tempId)
        self.sm.click_sendthrough()
        self.sm.enter_msg(msg)
        self.sm.select_msgto()
        self.sm.click_send()
        self.sm.get_success_msg()

    @pytest.mark.parametrize("title,msg", get_data("SendMsgData.xlsx", "PartialMsg"))
    def test_partial_msg(self,title,msg):
        self.sm = SendMsgAction(self.driver)
        self.sm.enter_title(title)
        self.sm.enter_msg(msg)
        self.sm.click_send()
        self.sm.get_missing_field_msg()

    def test_empty_msg(self):
        self.sm = SendMsgAction(self.driver)
        self.sm.click_send()
        self.sm.get_error_msg()