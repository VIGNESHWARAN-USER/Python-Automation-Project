import pytest
from actions.inventory_actions import Inventoryaction
from actions.login_action import LoginAction
from utilities.download_checker import clear_downloads, is_file_downloaded


@pytest.mark.muhindhar
@pytest.mark.usefixtures("setup_and_teardown")
class TestInventory:

    @pytest.mark.flaky(reruns=2)
    def test_inventory_stocklist(self):
        login = LoginAction(self.driver)
        inva = Inventoryaction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        inva.clk_inventory()
        assert inva.check_stocklist(), "Item Stock List is not displayed"

    def test_inventory_issueitem(self):
        login = LoginAction(self.driver)
        inva = Inventoryaction(self.driver)
        login.click_login("Receptionist")
        login.click_login_button()
        inva.clk_inventory()
        inva.click_issueitem()
        assert inva.check_issueitemlist(), "Issue Item List is not displayed"

    @pytest.mark.flaky(reruns=2)
    def test_inventory_excel_download(self):
        login = LoginAction(self.driver)
        inva = Inventoryaction(self.driver)
        clear_downloads()
        login.click_login("Receptionist")
        login.click_login_button()
        inva.clk_inventory()
        inva.clk_excel()
        assert is_file_downloaded(".xlsx"), "Excel file was not downloaded"

    @pytest.mark.flaky(reruns=2)
    def test_inventory_csv_download(self):
        login = LoginAction(self.driver)
        inva = Inventoryaction(self.driver)
        clear_downloads()
        login.click_login("Receptionist")
        login.click_login_button()
        inva.clk_inventory()
        inva.clk_csv()
        assert is_file_downloaded(".csv"), "CSV file was not downloaded"

    @pytest.mark.flaky(reruns=2)
    def test_inventory_pdf_download(self):
        login = LoginAction(self.driver)
        inva = Inventoryaction(self.driver)
        clear_downloads()
        login.click_login("Receptionist")
        login.click_login_button()
        inva.clk_inventory()
        inva.clck_pdf()
        assert is_file_downloaded(".pdf"), "PDF file was not downloaded"
