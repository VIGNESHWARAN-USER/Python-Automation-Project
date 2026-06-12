import pytest
import utilities.excel_reader as excelreader
from actions.complaint_action import ComplaintActions
from actions.login_action import LoginAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("complainttype,source,complainby,phone,date,description,actiontaken,assigned,note",excelreader.get_data("ComplaintData.xlsx", "Sheet1"),)
class TestComplaint:

    def test_complaint(self,complainttype,source,complainby,phone,date,description,actiontaken,assigned,note,):
        login = LoginAction(self.driver)
        complaint = ComplaintActions(self.driver)
        try:
            login.click_login("Receptionist")
            login.click_login_button()

            complaint.clkfo()
            complaint.clkcom()
            complaint.addcomp()

            complaint.compdet(complainttype,source,complainby,phone,date,description,actiontaken,assigned,note,)
            complaint.savebtn()
            actual_text = complaint.checklistcom()

            assert (actual_text == "Complain List"), f"Expected 'Complain List' but got '{actual_text}'"
        except Exception as e:
            complaint.take_screenshot("complaint_failure")
            pytest.fail(f"Complaint Test Failed. Error: {str(e)}")
