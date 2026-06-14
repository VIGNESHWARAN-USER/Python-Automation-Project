import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.OPDPage import OPDPage
from utilities.csvreader import get_data

logger = logging.getLogger(__name__)


class OPDDischargeAction:
    def __init__(self, driver):
        self.driver = driver
        self.opd_page = OPDPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_opd_page(self):
        logger.info("Navigating to OPD page via sidebar")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.opd_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.opd_page.old_opd_tab)).click()

    def click_patient_id_link(self):
        logger.info("Clicking patient ID link")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.opd_out_patient_nav_link)).click()

    def click_discharge_icon(self):
        logger.info("Clicking discharge icon")
        self.wait.until(EC.element_to_be_clickable(self.opd_page.discharge_icon)).click()

    def fill_discharge_form(self):
        logger.info("Filling discharge form from CSV")
        rows = get_data("discharge_data.csv")
        row = rows[0]

        date_input = self.wait.until(EC.visibility_of_element_located(self.opd_page.date_field))
        date_input.click()
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(row[0])
        date_input.send_keys(Keys.ESCAPE)

        status_el = self.wait.until(EC.element_to_be_clickable(self.opd_page.reason_dropdown))

        self.wait.until(lambda d: len(Select(status_el).options) > 1)

        actual_options = [o.text for o in Select(status_el).options]
        logger.info(f"Dropdown options: {actual_options}")
        logger.info(f"CSV value to select: '{row[1]}'")

        Select(status_el).select_by_visible_text(row[1])

        self.driver.find_element(*self.opd_page.note_field).send_keys(row[2])
        self.driver.find_element(*self.opd_page.operation_field).send_keys(row[3])
        self.driver.find_element(*self.opd_page.diagnosis_field).send_keys(row[4])
        self.driver.find_element(*self.opd_page.investigation_field).send_keys(row[5])

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