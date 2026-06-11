# tests/opd_add_patient_test.py

import pytest
from utilities.excel_reader import get_data
from actions.login_action import LoginAction
from actions.OPD_AddPatient_Action import OPDAddPatientActions

@pytest.mark.jerishwin
@pytest.mark.usefixtures("setup_and_teardown")
class TestOPDAddPatient:

    FILE_NAME  = "OPDTestData.xlsx"
    SHEET_NAME = "Sheet1"          # ← update to your actual sheet name

    def _login(self):
        login = LoginAction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()

    def _get_row_as_dict(self, row_index: int) -> dict:
        rows = get_data(self.FILE_NAME, self.SHEET_NAME)
        return {
            "Name":   rows[row_index][0],
            "Gender": rows[row_index][1],
            "Year":   rows[row_index][2],
            "Month":  rows[row_index][3],
            "Day":    rows[row_index][4],
        }

    def test_add_patient_from_excel(self):
        self._login()
        apa = OPDAddPatientActions(self.driver)

        apa.navigate_to_opd_page()          # ← sidebar click
        apa.click_add_patient_button()      # ← tab_2 button
        apa.click_add_icon()                # ← modal add icon
        apa.fill_patient_form_from_excel()  # ← rows[0] from Excel
        apa.click_save()

        assert apa.is_success_message_displayed(), \
            "Expected 'Record Saved Successfully' message not displayed"

    def test_add_patient_without_name_shows_error(self):
        self._login()
        apa  = OPDAddPatientActions(self.driver)
        data = self._get_row_as_dict(row_index=1)   # rows[1] — Name is empty
        print(f"Test Data: {data}")

        apa.navigate_to_opd_page()
        apa.click_add_patient_button()
        apa.click_add_icon()
        apa.fill_patient_form(data)
        apa.click_save()

        assert apa.is_name_error_displayed(), \
            "Expected 'Name field is required' error not displayed"