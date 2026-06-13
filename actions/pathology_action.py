from actions.base_action import BaseAction
from pages.pathology_page import PathalogyPage
from pages.sidebar_page import SideBarPage
from pages.patient_login_page import PatientLoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.logger import get_logger

logger = get_logger()

class PathalogyAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.pp = PathalogyPage()
        self.sp = SideBarPage()
        self.plp = PatientLoginPage()
        self.wait = WebDriverWait(driver, 10)

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

    # payment    
    def click_pay(self, billNo):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.paybtn))
            self.select_by_text(self.pp.paybtn, billNo)
        except Exception as e:
            logger.error(f"failed to click pay button: {str(e)}")

    def enter_amount(self, amt):
        try:
            return self.send_keys(self.pp.payAmt,amt)
        except Exception as e:
            logger.error(f"failed to enter amount: {str(e)}")
                    
    def click_add(self):
        try:
            self.click(self.pp.add)
        except Exception as e:
            logger.error(f"failed to click add button: {str(e)}")

    def ensure_makepay(self,driver):
        try:
            self.click(self.pp.makepay)
            self.driver.switch_to.frame(self.pp.frame)
        except Exception as e:
            logger.error(f"failed to click add button: {str(e)}")

    def enter_mobile(self, mobile):
        try:
            self.send_keys(self.pp.mobile, mobile)
        except Exception as e:
            logger.error(f"failed to click add button: {str(e)}")

    def click_continue(self):
        try:
            self.click(self.pp.cont)
        except Exception as e:
            logger.error(f"failed to click continue button: {str(e)}")

    def choose_upi(self):
        try:
            self.click(self.pp.upi)
        except Exception as e:
            logger.error(f"failed to click upi option: {str(e)}")

    def send_upiId(self):
        try:
            self.click(self.pp.makepay)
        except Exception as e:
            logger.error(f"failed to click add button: {str(e)}")

    def click_verify(self):
        try:
            self.click(self.pp.verify)
        except Exception as e:
            logger.error(f"failed to click verify button: {str(e)}")

    def get_success_txt(self,driver):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            logger.error(f"Already on main page: {str(e)}")
        try:
            return self.get_text(self.pp.succ)
        except Exception as e:
            logger.error(f"Success message not found on page: {str(e)}")

    def get_pay_error_txt(self, driver):
        try:
            return self.get_text(self.pp.payError)
        except TimeoutException:
            page_source = self.driver.page_source
            has_exceed = "Amount Should Not Be Greater Than Balance" in page_source
            has_invalid = "Invalid Amount" in page_source
            if has_exceed:
                return "Amount Should Not Be Greater Than Balance"
            if has_invalid:
                return "Invalid Amount"
            return ""      
                                           