from actions.base_action import BaseAction
from pages.pathology_page import PathalogyPage
from pages.sidebar_page import SideBarPage
from pages.patient_login_page import PatientLoginPage
from utilities.logger import get_logger

logger = get_logger()

class PathalogyAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.pp = PathalogyPage()
        self.sp = SideBarPage()
        self.plp = PatientLoginPage()

    def click_user_login(self):
        try:
           self.click(self.plp.userlog)
        except Exception as e:
            logger.error(f"failed to click user login: {str(e)}")

    def click_signup(self):
        try:
           self.click(self.plp.signup)
        except Exception as e:
            logger.error(f"failed to click signup button: {str(e)}")

    def click_pathology_menu(self):
        try:
           self.js_click(self.sp.pathlogyMenu)
        except Exception as e:
            logger.error(f"failed to click pathology menu: {str(e)}")

    def search_report(self, billno):
        self.send_keys(self.pp.search, str(billno))
    
    def is_rec_displaced(self, billno):
        try:
            return self.is_displayed(self.pp.get_record_locator(billno))
        except Exception as e:
            logger.error(f"record is not displayed: {str(e)}")

    def is_displayed_errormsg(self, billNo):
        try:
            return self.is_displayed(self.pp.notFound)
        except Exception as e:
            logger.error(f"failed to handle invalid search: {str(e)}")
                        