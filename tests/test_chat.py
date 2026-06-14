import pytest
from actions.chat_appointment_action import Chataction
from actions.login_action import LoginAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class TestChatAppointment:
    @pytest.mark.flaky(reruns=2)
    def test_chatappointment(self):
        login = LoginAction(self.driver)
        chat = Chataction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        chat.clickappointment()
        chat.clickchaticon()
        chat.selectdoctor()
        chat.sendmessage()
        assert chat.verifymessage(), "Chat message verification failed"

    def test_chat_page_open(self):
        login = LoginAction(self.driver)
        chat = Chataction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        chat.clickappointment()
        chat.clickchaticon()
        assert chat.is_displayed(chat.cap.person), "Doctor list is not displayed"