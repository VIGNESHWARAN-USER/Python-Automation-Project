# actions/OPD_AddPatient_Action.py

import logging
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pages.OPDPage import OPDPage
from utilities.excel_reader import get_data

logger = logging.getLogger(__name__)


class OPDAddPatientActions:

    FILE_NAME  = "OPDTestData.xlsx"
    SHEET_NAME = "Sheet1"          # ← update to your actual sheet name

    def __init__(self, driver):
        self.driver   = driver
        self.opd_page = OPDPage(driver)
        self.wait     = WebDriverWait(driver, 15)

    # ── Navigation ───────────────────────────────────────────────────────────

    def navigate_to_opd_page(self):
        self.wait.until(EC.element_to_be_clickable(self.opd_page.opd_button))
        self.driver.find_element(*self.opd_page.opd_button).click()
        logger.info("Clicked OPD sidebar button")

    # ── Clicks ───────────────────────────────────────────────────────────────

    def click_add_patient_button(self):
        self.wait.until(EC.element_to_be_clickable(self.opd_page.add_patient_button))
        self.driver.find_element(*self.opd_page.add_patient_button).click()
        logger.info("Clicked Add Patient button")

    def click_add_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.opd_page.add_icon))
        self.driver.find_element(*self.opd_page.add_icon).click()
        logger.info("Clicked Add icon")

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.opd_page.save_button))
        self.driver.find_element(*self.opd_page.save_button).click()
        logger.info("Clicked Save button")

    # ── Form Filling ─────────────────────────────────────────────────────────

    def fill_patient_form(self, data: dict):
        name   = data.get("Name")
        gender = data.get("Gender")
        year   = data.get("Year")
        month  = data.get("Month")
        day    = data.get("Day")

        self.wait.until(EC.visibility_of_element_located(self.opd_page.name_field))

        if name:
            self.driver.find_element(*self.opd_page.name_field).clear()
            self.driver.find_element(*self.opd_page.name_field).send_keys(name)

        if gender:
            gender_el = self.driver.find_element(*self.opd_page.gender_dropdown)
            Select(gender_el).select_by_visible_text(gender)

        if year:
            self.driver.find_element(*self.opd_page.year_field).clear()
            self.driver.find_element(*self.opd_page.year_field).send_keys(str(year))

        if month:
            self.driver.find_element(*self.opd_page.month_field).clear()
            self.driver.find_element(*self.opd_page.month_field).send_keys(str(month))

        if day:
            self.driver.find_element(*self.opd_page.day_field).clear()
            self.driver.find_element(*self.opd_page.day_field).send_keys(str(day))

    def fill_patient_form_from_excel(self):
        rows = get_data(self.FILE_NAME, self.SHEET_NAME)
        data = {
            "Name":   rows[0][0],
            "Gender": rows[0][1],
            "Year":   rows[0][2],
            "Month":  rows[0][3],
            "Day":    rows[0][4],
        }
        print(f"Excel Data Loaded: {data}")
        self.fill_patient_form(data)

    # ── Verifications ─────────────────────────────────────────────────────────

    def is_success_message_displayed(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.opd_page.success_message))
            logger.info("Success message displayed")
            return True
        except Exception:
            logger.warning("Success message NOT displayed")
            return False

    def is_name_error_displayed(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.opd_page.name_error_message))
            logger.info("Name error message displayed")
            return True
        except Exception:
            logger.warning("Name error message NOT displayed")
            return False