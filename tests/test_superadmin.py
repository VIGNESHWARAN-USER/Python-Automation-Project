from actions.superadmin_action import Superadminaction
from actions.login_action import LoginAction
import pytest
import utilities.excel_reader as excelreader


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class Testsuperadmin:

    def test_opd(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        sa.opd()

    def test_ipd(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.ipd()

    @pytest.mark.skip(reason="Pharmacy module under development")
    @pytest.mark.parametrize("medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note",excelreader.get_data("medicallist.xlsx", "Sheet1"))
    def test_pharmacy(self,medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.medicine_details(medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note)
        
    def test_pathology(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.pathology()

    def test_radiology(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.radiology()
        
    #fails because during testing some of the options are not showing 
    def test_bloodbank(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.bloodbank()

    def test_ambulance(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.ambulance()

    def test_general(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.general()

    def test_expense(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.expenses()