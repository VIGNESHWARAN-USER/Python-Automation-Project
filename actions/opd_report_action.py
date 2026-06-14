# actions/opd_report_action.py
import os
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.OPDPage import OPDPage

logger = logging.getLogger(__name__)


class OPDReportAction:
    def __init__(self, driver):
        self.driver = driver
        self.opd_page = OPDPage(driver)
        self.wait = WebDriverWait(driver, 15)
        self._enable_headless_downloads()

    # --- private helper ---
    def _js_click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", el)

    def _enable_headless_downloads(self):
        download_path = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_path, exist_ok=True)
        self.driver.execute_cdp_cmd(
            "Browser.setDownloadBehavior",
            {
                "behavior":     "allow",
                "downloadPath": download_path
            }
        )
        logger.info(f"Headless download path set to: {download_path}")

    # Background: "And the user is on the OPD Out-Patient page"
    def navigate_to_opd_out_patient_page(self):
        logger.info("Opening OPD page")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.opd_button)).click()
        logger.info("Clicking Old OPD tab")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.old_opd_tab)).click()

    def click_show_icon(self):
        logger.info("Clicking ID Link")
        self._js_click(self.opd_page.opd_out_patient_nav_link)

    # And: "clicks the Visits tab"
    def click_visits_tab(self):
        logger.info("Clicking visits tab")
        self._js_click(self.opd_page.visits_tab)

    # And: "clicks the Print / PDF icon"
    def click_print_icon(self):
        logger.info("Clicking PDF icon")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.print_icon))
        self.driver.find_element(*self.opd_page.print_icon).click()

    # Then: "the report is downloaded successfully"
    def is_report_downloaded_successfully(self) -> bool:
        download_path = os.path.join(os.getcwd(), "downloads")
        timeout = time.time() + 15
        while time.time() < timeout:
            if os.path.exists(download_path):
                for filename in os.listdir(download_path):
                    name = filename.lower()
                    if name.endswith(".pdf") and ".crdownload" not in name:
                        logger.info(f"PDF found: {filename}")
                        return True
            time.sleep(1)
        logger.warning(f"No PDF found in: {download_path}")
        return False