import pytest
from actions.chat_appointment_action import Chataction
from actions.login_action import LoginAction

@pytest.mark.usefixtures("setup_and_teardown")
class TestChatAppointment:
    def test_chatappointment(self):
        login=LoginAction(self.driver)
        chat= Chataction(self.driver)
        try:
            login.click_login("Receptionist")
            login.click_login_button()
            chat.clickappointment()
            chat.clickchaticon()
            chat.selectdoctor()
            chat.sendmessage()
            assert chat.verifymessage(), "Chat message verification failed"
        except Exception as e:
            chat.take_screenshot("chat_appointment_failure")
            pytest.fail(f"Chat Appointment Test Failed. " f"Error: {str(e)}")
