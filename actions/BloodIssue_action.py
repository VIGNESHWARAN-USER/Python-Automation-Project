from actions.base_action import BaseAction
from pages.BloodIssue_page import BloodIssue
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()

class BloodIssueAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.bp = BloodIssue()
        self.sp = SideBarPage()
        self.wait = WebDriverWait(driver, 10)

    def click_AccImg(self):
        try:
            self.click(self.bp.profile)
            logger.info("Successfully clicked Profile")
        except Exception as e:
            logger.error(f"failed to click profile: {str(e)}")

    def get_AccName(self):
        try:
            self.get_text(self.bp.pathologylog)
            logger.info("Successfully get text from pathology login")
        except Exception as e:
            logger.error(f"failed to get text from pathology login: {str(e)}")

    def click_bloodbank(self):
        try:
            self.click(self.sp.bloodbank)
            logger.info("Successfully clicked blood bank menu")
        except Exception as e:
            logger.error(f"failed to click blood bank menu: {str(e)}")

    def isDisplayed_status(self):
        try:
            self.is_displayed(self.bp.status)
            logger.info("Successfully displayed blood bank status")
        except Exception as e:
            logger.error(f"failed to displayed blood bank status: {str(e)}")

    def click_blood(self):
        try:
            self.click(self.bp.blood)
            logger.info("Successfully click the blood type")
        except Exception as e:
            logger.error(f"failed to click the blood type: {str(e)}")

    def click_IssueBtn(self):
        try:
            self.click(self.bp.issue)
            logger.info("Successfully clicked issue button")
        except Exception as e:
            logger.error(f"failed to click issue button: {str(e)}")

    def isDisplayed_Form(self):
        try:
            self.is_displayed(self.bp.form)
            logger.info("Successfully displayed the form")
        except Exception as e:
            logger.error(f"failed to displayed the form: {str(e)}")      