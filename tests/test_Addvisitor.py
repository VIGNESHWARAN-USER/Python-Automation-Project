import pytest
from actions.AddVisitorActions import AddvisiorActions
from utilities import csvreader


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.parametrize(
    "name,phone,idcard,noofperson,note", csvreader.get_data("addvisitordata.csv")
)
class TestAddVisitor:

    def test_addvisitor(self, name, phone, idcard, noofperson, note):

        adv = AddvisiorActions(self.driver)

        adv.clk_recpbtn()
        adv.clk_signin()
        adv.clck_frontofc()

        adv.add_inp(name, phone, idcard, noofperson, note)

        adv.clk_savebtn()

        assert adv.check_list()
