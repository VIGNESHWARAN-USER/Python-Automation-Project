import pytest
from actions.superadmin_action import Superadminaction
from actions.login_action import LoginAction
import utilities.excel_reader as excelreader

@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class Testsuperadmin:

    #@pytest.mark.dependency(name="opd")
    def test_opd(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        sa.opd()

    @pytest.mark.dependency(name="ipd", depends=["opd"])
    def test_ipd(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.ipd()

    '''@pytest.mark.dependency(name="pharmacy", depends=["ipd"])
    @pytest.mark.skip(reason="skipping due to the project is under development")
    @pytest.mark.parametrize("medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note",excelreader.get_data("medicallist.xlsx", "Sheet1"),)
    def test_pharmacy(self,medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note,):

        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()

        assert sa.medicine_details(medicalname,composition,minlevel,reorderlevel,tax,vatac,racknumber,boxpacking,note,)'''

    @pytest.mark.dependency(name="pathology", depends=["ipd"])
    def test_pathology(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.pathology()

    @pytest.mark.dependency(name="radiology", depends=["pathology"])
    def test_radiology(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.radiology()

    @pytest.mark.dependency(name="bloodbank", depends=["radiology"])
    def test_bloodbank(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.bloodbank()

    @pytest.mark.dependency(name="ambulance", depends=["bloodbank"])
    def test_ambulance(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.ambulance()

    @pytest.mark.dependency(name="general", depends=["ambulance"])
    def test_general(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.general()

    @pytest.mark.dependency(name="expense", depends=["general"])
    def test_expense(self):
        lp = LoginAction(self.driver)
        sa = Superadminaction(self.driver)
        lp.click_login("Super Admin")
        lp.click_login_button()
        assert sa.expenses()
