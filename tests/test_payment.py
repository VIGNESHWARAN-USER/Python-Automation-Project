import pytest
from actions.pathology_action import PathalogyAction
from utilities.excel_reader import get_data

@pytest.mark.mythily
@pytest.mark.usefixtures("setup_and_teardown")
class TestPayment:

    @pytest.fixture(autouse=True)
    def setup(self, setup_and_teardown):
        self.pa = PathalogyAction(self.driver)
        self.pa.click_user_login()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.pa.click_signup()
        self.pa.click_pathology_menu()

    @pytest.mark.parametrize("billno,amt,mobile,upiId", get_data("payment_data.xlsx", "validPay"))
    def test_valid_pay(self, billno, amt, mobile, upiId):
        self.pa.search(billno)
        self.pa.click_pay()
        self.pa.enter_amount(amt)
        self.pa.click_add()
        self.pa.ensure_makepay()
        self.pa.enter_mobile(mobile)
        self.pa.click_continue()
        self.pa.choose_upi()
        self.pa.send_upiId(upiId)
        self.pa.click_verify()
        succ = self.pa.get_success_txt()
        assert succ is not None
        
    @pytest.mark.parametrize("billno,amt,mobile,upiId", get_data("payment_data.xlsx", "exceedPay"))
    def test_exceed_amount_pay(self, billno, amt, mobile, upiId):
        self.pa.search(billno)
        self.pa.click_pay()
        self.pa.enter_amount(amt)
        self.pa.click_add()
        exceed = self.pa.get_pay_error_txt()
        assert "Amount Should Not Be Greater Than Balance" in exceed

    @pytest.mark.parametrize("billno,amt,mobile,upiId", get_data("payment_data.xlsx", "invalidPay"))
    def test_invalid_amount_pay(self, billno, amt, mobile, upiId):
        self.pa.search(billno)
        self.pa.click_pay()
        self.pa.enter_amount(amt)
        self.pa.click_add()
        invalid = self.pa.get_pay_error_txt()
        assert "Invalid Amount" in invalid