import pytest

from actions.login_action import LoginAction
from actions.notification_action import NotificationAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestNotification:

    @pytest.fixture(autouse=True)
    def setup(self, setup_and_teardown):
        self.la = LoginAction(self.driver)
        self.na = NotificationAction(self.driver)

        self.la.click_login("Doctor")
        self.la.click_login_button()

    def test_ipd_notification(self):
        self.na.click_notification()
        self.na.search_notification("IPD")

        assert self.na.is_ipd_notification_displayed(), \
            "IPD notification is not displayed"
