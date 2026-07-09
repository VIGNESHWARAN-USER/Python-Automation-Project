import pytest
from actions.base_action import BaseAction
from pages.blood_component_page import BloodComponentPage
from utilities.logger import get_logger

logger = get_logger()


class BloodComponentAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.bcp = BloodComponentPage()

    def click_billing(self):
        try:
            logger.info("Clicking Billing")
            self.click(self.bcp.billing)

        except Exception as e:
            self.take_screenshot("billing_click_failure")
            pytest.fail(f"Unable to click Billing. Error: {str(e)}")

    def click_blood_component(self):
        try:
            logger.info("Clicking Blood Component Issue")
            self.click(self.bcp.bloodcomp)

        except Exception as e:
            self.take_screenshot("blood_component_click_failure")
            pytest.fail(f"Unable to click Blood Component Issue. Error: {str(e)}")

    def click_details(self):
        try:
            logger.info("Clicking Patient Details")
            self.js_click(self.bcp.details)

        except Exception as e:
            self.take_screenshot("patient_details_failure")
            pytest.fail(f"Unable to click Patient Details. Error: {str(e)}")

    def verify_details(self):
        try:
            logger.info("Verifying Blood Component Issue Details")

            status = self.is_displayed(self.bcp.patientpopup)

            logger.info(f"Blood Component popup displayed: {status}")

            return status

        except Exception as e:
            self.take_screenshot("blood_component_popup_failure")
            pytest.fail(f"Blood Component popup verification failed. Error: {str(e)}")