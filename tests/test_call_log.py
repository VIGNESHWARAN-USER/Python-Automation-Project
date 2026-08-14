import pytest
import utilities.excel_reader as excelreader
from actions.call_log_action import CallLogFrontofcActions
from actions.login_action import LoginAction


@pytest.mark.malavicka
@pytest.mark.usefixtures("setup_and_teardown")
class TestCallLog:
    @pytest.mark.parametrize("name,phone,description,calltype,note,duration",excelreader.get_data("CallLogData.xlsx", "Sheet1"),)
    @pytest.mark.flaky(reruns=2)
    def test_calllog( self,name,phone,description,calltype,note,duration):
        login = LoginAction(self.driver)
        calllog = CallLogFrontofcActions(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        calllog.frontofclink()
        calllog.phcalllog()
        calllog.addcall()
        calllog.enterdet(name,phone,description,calltype,note,duration)
        calllog.clicksave()
        assert ("Phone Call Log" in calllog.checklist()), f"Phone Call Log page not displayed for data: {name}"

    def test_calllog_empty_fields(self):
        login = LoginAction(self.driver)
        calllog = CallLogFrontofcActions(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        calllog.frontofclink()
        calllog.phcalllog()
        calllog.addcall()
        calllog.clicksave()
        assert calllog.emptyfields(),"Required field validation message not displayed"