import pytest
from actions.pathology_action import PathalogyAction
from utilities.config_reader import get_value

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    
    @pytest.fixture(autouse=True)
    def setup(self, setup_and_teardown):
        self.pa = PathalogyAction(self.driver)
        self.pa.click_user_login()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.pa.click_signup()
        self.pa.click_pathology_menu()

    @pytest.mark.parametrize("billno", [get_value("./data_files/search.ini", "Valid Search", "billno")])
    def test_valid_search(self, billno):
        self.pa.search_report(billno)
        assert self.pa.is_rec_displaced(billno)

    @pytest.mark.parametrize("billno", [get_value("./data_files/search.ini", "Invalid Search", "billno")])
    def test_invalid_search(self, billno):
        self.pa.search_report(billno)
        assert self.pa.is_displayed_errormsg(billno) is True