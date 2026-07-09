import pytest
from actions.login_action import LoginAction
from actions.blood_component_action import BloodComponentAction


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class TestBloodComponent:

    def test_blood_component_details(self):

        login = LoginAction(self.driver)
        blood = BloodComponentAction(self.driver)

        login.click_login("Receptionist")
        login.click_login_button()

        blood.click_billing()
        blood.click_blood_component()
        blood.click_details()

        assert blood.verify_details(), \
            "Blood Component Issue Details popup is not displayed"