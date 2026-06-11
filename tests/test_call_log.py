import pytest
import utilities.excel_reader as excelreader
from actions.call_log_action import CallLogFrontofcActions
from actions.login_action import LoginAction


@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("name,phone,description,calltype,note,duration",excelreader.get_data("CallLogData.xlsx", "Sheet1"),)
class TestCallLog:

    def test_calllog(self, name, phone, description, calltype, note, duration):
        login = LoginAction(self.driver)
        calllog = CallLogFrontofcActions(self.driver)

        try:
            login.click_login("Receptionist")
            login.click_login_button()

            calllog.frontofclink()
            calllog.phcalllog()
            calllog.addcall()
            calllog.enterdet(name, phone, description, calltype, note, duration)
            calllog.clicksave()
            assert ("Phone Call Log" in calllog.checklist()), f"Phone Call Log page not displayed for data: {name}"
        except Exception as e:
            calllog.take_screenshot(f"call_log_failure_{name}")
            pytest.fail(f"Call Log Test Failed for '{name}'. " f"Error: {str(e)}")
