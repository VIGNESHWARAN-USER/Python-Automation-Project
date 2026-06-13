import pytest
import utilities.excel_reader as excelreader
from actions.complaint_action import ComplaintActions
from actions.login_action import LoginAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class TestComplaint:

    @pytest.mark.parametrize(
        "complainttype,source,complainby,phone,date,description,actiontaken,assigned,note",
        excelreader.get_data("ComplaintData.xlsx", "Sheet1"),
    )
    def test_complaint(
        self,
        complainttype,
        source,
        complainby,
        phone,
        date,
        description,
        actiontaken,
        assigned,
        note,
    ):
        login = LoginAction(self.driver)
        complaint = ComplaintActions(self.driver)

        login.click_login("Receptionist")
        login.click_login_button()

        complaint.clkfo()
        complaint.clkcom()
        complaint.addcomp()

        complaint.compdet(
            complainttype,
            source,
            complainby,
            phone,
            date,
            description,
            actiontaken,
            assigned,
            note,
        )

        complaint.savebtn()

        actual_text = complaint.checklistcom()

        assert (
            actual_text == "Complain List"
        ), f"Expected 'Complain List' but got '{actual_text}'"

    def test_complaint_empty_fields(self):

        login = LoginAction(self.driver)
        complaint = ComplaintActions(self.driver)

        login.click_login("Receptionist")
        login.click_login_button()

        complaint.clkfo()
        complaint.clkcom()
        complaint.addcomp()
        complaint.savebtn()

        assert (
            complaint.emptyfields()
        ), "Required field validation message not displayed"
