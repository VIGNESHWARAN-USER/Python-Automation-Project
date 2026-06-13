import pytest
from actions.login_action import LoginAction
from actions.profile_action import ProfileAction

@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestAttendanceReport:

    @pytest.mark.parametrize("role", ["Doctor", "Receptionist", "Admin", "Nurse"])
    def test_view_attendance_report(self, role):
        la = LoginAction(self.driver)
        pa = ProfileAction(self.driver)

        # Given - user logs in
        la.click_login(role)
        la.click_login_button()

        # When - navigate to attendance report
        pa.click_profile_icon()
        pa.click_profile_button()
        pa.click_leave_button()

        # Then - leave/attendance table is visible
        assert pa.is_leave_table(), "Attendance report table not found"