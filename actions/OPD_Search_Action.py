from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.OPDPage import OPDPage
from actions.base_action import BaseAction
import logging

logger = logging.getLogger(__name__)


class OPDSearchActions(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.opd_page = OPDPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def search_patient(self, patient_name):
        logger.info("Passing patient name")
        self.send_keys(self.opd_page.search_box, patient_name)

    def navigate_to_opd_page(self):
        self.wait.until(
            EC.element_to_be_clickable(self.opd_page.opd_button)
        )

        logger.info("Clicking OPD button")
        self.js_click(self.opd_page.opd_button)

        self.wait.until(
            EC.element_to_be_clickable(self.opd_page.old_opd_tab)
        )

        logger.info("Clicking Old OPD tab")
        self.js_click(self.opd_page.old_opd_tab)

    def verify_search_name_result(self):
        self.wait.until(
            EC.visibility_of_element_located(self.opd_page.patient_name)
        )

        logger.info("Getting patient name")
        return self.get_text(self.opd_page.patient_name)

    def verify_search_failed(self):
        self.wait.until(
            EC.visibility_of_element_located(self.opd_page.search_failed)
        )

        logger.info("Search failed")
        return self.get_text(self.opd_page.search_failed)