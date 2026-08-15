import pytest
from actions.BloodIssue_action import BloodIssueAction
from actions.login_action import LoginAction

@pytest.mark.mythily
@pytest.mark.usefixtures("setup_and_teardown")
class TestBloodIssue:
    
    def test_blood_issue(self):
        self.ba = BloodIssueAction(self.driver)
        self.la = LoginAction(self.driver)
        self.la.click_login("Pathologist")
        self.la.click_login_button()
        self.ba.click_AccImg()
        self.ba.get_AccName()
        self.ba.click_bloodbank()
        self.ba.isDisplayed_status()
        self.ba.click_blood()
        self.ba.click_IssueBtn()
        self.ba.isDisplayed_Form()