from selenium.webdriver.support.ui import Select

from actions.base_action import BaseAction
from pages.certificate_page import CertificatePage
from utilities.csvreader import get_data
from utilities.logger import get_logger


logger = get_logger()


class CertificateAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.cp = CertificatePage()

    def click_certificate_menu(self):
        try:
            logger.info("Clicking certificate menu")
            self.click(self.cp.certificate_menu)
        except Exception as e:
            logger.error(f"Failed to click certificate menu: {str(e)}")
            raise

    def click_certificate_sub_menu(self):
        try:
            logger.info("Clicking certificate sub menu")
            self.click(self.cp.certificate_sub_menu)
        except Exception as e:
            logger.error(f"Failed to click certificate sub menu: {str(e)}")
            raise

    def select_valid_certificate_details(self):
        try:
            logger.info("Selecting valid certificate details")

            data = get_data("CertificateData.csv")
            valid_data = data[0]

            module = valid_data[0]
            status = valid_data[1]
            template = valid_data[2]

            Select(
                self.wait_for_visibility(
                    self.cp.module_dropdown
                )
            ).select_by_visible_text(module)

            Select(
                self.wait_for_visibility(
                    self.cp.patient_status_dropdown
                )
            ).select_by_visible_text(status)

            Select(
                self.wait_for_visibility(
                    self.cp.certificate_template_dropdown
                )
            ).select_by_visible_text(template)

        except Exception as e:
            logger.error(
                f"Failed to select valid certificate details: {str(e)}"
            )
            raise

    def select_invalid_certificate_details(self):
        try:
            logger.info("Selecting invalid certificate details")

            data = get_data("CertificateData.csv")
            invalid_data = data[1]

            module = invalid_data[0]
            status = invalid_data[1]
            template = invalid_data[2]

            Select(
                self.wait_for_visibility(
                    self.cp.module_dropdown
                )
            ).select_by_visible_text(module)

            Select(
                self.wait_for_visibility(
                    self.cp.patient_status_dropdown
                )
            ).select_by_visible_text(status)

            Select(
                self.wait_for_visibility(
                    self.cp.certificate_template_dropdown
                )
            ).select_by_visible_text(template)

        except Exception as e:
            logger.error(
                f"Failed to select invalid certificate details: {str(e)}"
            )
            raise

    def click_search_button(self):
        try:
            logger.info("Clicking search button")
            self.click(self.cp.search_button)
        except Exception as e:
            logger.error(f"Failed to click search button: {str(e)}")
            raise

    def select_patient(self):
        try:
            logger.info("Selecting patient")

            data = get_data("CertificateData.csv")
            patient_name = data[0][3]

            self.click(
                self.cp.get_patient_checkbox_locator(patient_name)
            )

        except Exception as e:
            logger.error(f"Failed to select patient: {str(e)}")
            raise


    def click_generate_button(self):
        try:
            logger.info("Clicking generate button")
            self.click(self.cp.generate_button)
        except Exception as e:
            logger.error(f"Failed to click generate button: {str(e)}")
            raise

    def close_patient_details_page(self):
        try:
            logger.info("Closing patient details page")
            self.click(self.cp.close_details_page)
        except Exception as e:
            logger.error(f"Failed to close patient details page: {str(e)}")
            raise