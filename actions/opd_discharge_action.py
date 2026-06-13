# actions/opd_discharge_action.py

import logging
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.OPDPage import OPDPage
from utilities.csvreader import CSVReaderUtil

logger = logging.getLogger(__name__)

class OPDDischargeAction:

    def __init__(self, driver):
        self.driver = driver
        self.opd_page = OPDPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_patient_id_link(self):
        logger.info("Clicking revert and OPD nav link")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.revert)).click()
        self.wait.until(EC.element_to_be_clickable(self.opd_page.opd_out_patient_nav_link)).click()

    def click_discharge_icon(self):
        logger.info("Clicking discharge icon")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.discharge_icon)).click()

    def fill_discharge_form(self):
        logger.info("Filling discharge form")
        data = CSVReaderUtil.get_test_data_by_test_case("discharge_data", "DischargePatient")

        # Date
        date_input = self.wait.until(EC.visibility_of_element_located(self.opd_page.date_field))
        date_input.clear()
        date_input.send_keys(data["date"])

        # Reason dropdown
        reason_select = Select(self.driver.find_element(*self.opd_page.reason_drop_down))
        reason_select.select_by_visible_text(data["reason"])

        # Text areas
        self.driver.find_element(*self.opd_page.note_field).send_keys(data["note"])
        self.driver.find_element(*self.opd_page.operation_field).send_keys(data["operation"])
        self.driver.find_element(*self.opd_page.diagnosis_field).send_keys(data["diagnosis"])
        self.driver.find_element(*self.opd_page.investigation_field).send_keys(data["investigation"])

    def click_save_discharge_button(self):
        logger.info("Clicking save discharge button")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.save_discharge_button)).click()

    def is_success_message_displayed(self):
        logger.info("Checking success message")
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.opd_page.success_message)
            ).is_displayed()
        except Exception:
            return False