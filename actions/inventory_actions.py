from pages.inventory_page import inventory
from actions.base_action import BaseAction
from utilities.logger import get_logger
from pages.sidebar_page import SideBarPage
import pytest
from utilities.download_checker import is_file_downloaded
import pytest
logger = get_logger()

class Inventoryaction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.inva = inventory()
        self.side = SideBarPage()

    def clk_inventory(self):
        try:
            logger.info("Clicking Inventory menu")
            elements = self.driver.find_elements(*self.side.inventory)
            logger.info(f"Inventory Elements Found: {len(elements)}")
            self.scroll_and_click(self.side.inventory)
        except Exception as e:
            pytest.fail(f"Unable to click Inventory menu. Error: {str(e)}")

    def check_stocklist(self):
        try:
            logger.info("Verifying Item Stock List")
            status = self.is_displayed(self.inva.itemstocklist)
            logger.info(f"Item Stock List Displayed: {status}")
            return status
        except Exception as e:
            pytest.fail(f"Item Stock List not displayed. Error: {str(e)}")

    def click_issueitem(self):
        try:
            logger.info("Clicking Issue Item")
            self.click(self.inva.issueitem)
        except Exception as e:
            pytest.fail(f"Unable to click Issue Item. Error: {str(e)}")

    def check_issueitemlist(self):
        try:
            logger.info("Verifying Issue Item List")
            status = self.is_displayed(self.inva.issueitemlist)
            logger.info(f"Issue Item List Displayed: {status}")
            return status
        except Exception as e:
            pytest.fail(f"Issue Item List not displayed. Error: {str(e)}")

    def clk_excel(self):
        try:
            logger.info("Clicking Excel Export")
            self.click(self.inva.excel)
        except Exception as e:
            pytest.fail(f"Unable to click Excel Export. Error: {str(e)}")

    def clk_csv(self):
        try:
            logger.info("Clicking CSV Export")
            self.click(self.inva.csv)
        except Exception as e:
            pytest.fail(f"Unable to click CSV Export. Error: {str(e)}")

    def clck_pdf(self):
        try:
            logger.info("Clicking PDF Export")
            self.click(self.inva.pdf)
        except Exception as e:
            pytest.fail(f"Unable to click PDF Export. Error: {str(e)}")
            
    def verify_excel_download(self):
        try:
            return is_file_downloaded(".xlsx")

        except Exception as e:
            self.take_screenshot("excel_download_failure")
            pytest.fail(f"Excel download verification failed. Error: {str(e)}")

def verify_csv_download(self):
    try:
        return is_file_downloaded(".csv")

    except Exception as e:
        self.take_screenshot("csv_download_failure")
        pytest.fail(f"CSV download verification failed. Error: {str(e)}")

def verify_pdf_download(self):
    try:
        return is_file_downloaded(".pdf")

    except Exception as e:
        self.take_screenshot("pdf_download_failure")
        pytest.fail(f"PDF download verification failed. Error: {str(e)}")