import pytest
from utilities.config_reader import get_value
from actions.join_consultation_action import JoinConsultationAction
from actions.login_action import LoginAction

@pytest.mark.vigneshwaran
@pytest.mark.usefixtures("setup_and_teardown")
class TestJoinConsultation:

    @pytest.fixture(autouse=True)   
    def setup(self, setup_and_teardown):
        self.ca = JoinConsultationAction(self.driver)
        self.la = LoginAction(self.driver)
        self.la.click_login("Doctor")
        self.la.click_login_button()
        self.ca.click_live_consultation_dropdown()
        self.ca.click_live_consultation_option()
        

    def test_join_button_clickable(self):
        self.index = self.ca.find_record_with_status("Awaited")
        assert self.ca.is_action_present(self.index)
        assert self.ca.is_action_clickable(self.index), "The join button is not clickable"

    def test_join_button_is_not_visible(self):
        self.index = self.ca.find_record_not_with_status("Awaited")
        assert self.ca.is_action_not_present(self.index)

    def test_start_now_button_visible(self):
        self.index = self.ca.find_record_with_status("Awaited")
        self.ca.click_join_button(self.index)
        assert self.ca.is_popup_displayed()
        assert self.ca.is_start_now_button_displayed()

    def test_click_start_now_button_opens_zoom(self):
        self.index = self.ca.find_record_with_status("Awaited")
        self.ca.click_join_button(self.index)
        self.ca.click_start_now_button()
        assert self.ca.is_new_browser_opened()
        assert self.ca.is_url_contains(get_value("./data_files/consultation_data.ini", "data set", "meeting_link"))

        
    


    