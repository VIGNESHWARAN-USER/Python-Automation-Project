import pytest
from actions.login_action import LoginAction
from actions.profile_action import ProfileAction


@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestProfilePage:

    @pytest.mark.parametrize("role", ["Doctor", "Nurse", "Receptionist", "Admin"])
    def test_view_profile_details(self, role):
        la = LoginAction(self.driver)
        pa = ProfileAction(self.driver)

        la.click_login(role)
        la.click_login_button()

        pa.click_profile_icon()
        pa.click_profile_button()

        assert role in pa.get_role(), f"Expected '{role}' in profile role text"

