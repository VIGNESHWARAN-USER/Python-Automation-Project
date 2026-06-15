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
    def search(self, billno):
        self.send_keys(self.pp.search, str(billno))

    def click_pay(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.paybtn))
            self.click(self.pp.paybtn)
        except Exception as e:
            logger.error(f"failed to click pay button: {str(e)}")

    def enter_amount(self, amt):
        try:
            field = self.wait.until(EC.visibility_of_element_located(self.pp.payAmt))
            field.clear()                  
            field.send_keys(str(amt)) 
        except Exception as e:
            logger.error(f"failed to enter amount: {str(e)}")

    def click_add(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.add)) 
            self.js_click(self.pp.add) 
        except Exception as e:
            logger.error(f"failed to click add button: {str(e)}")

    def ensure_makepay(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.makepay))
            self.js_click(self.pp.makepay)                              
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.pp.frame))
        except Exception as e:
            logger.error(f"failed to click make payment: {str(e)}")

    def enter_mobile(self, mobile):
        try:
            self.wait.until(EC.visibility_of_element_located(self.pp.mobile))
            self.send_keys(self.pp.mobile, str(mobile))
        except Exception as e:
            logger.error(f"failed to enter mobile: {str(e)}")

    def click_continue(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.cont))
            self.js_click(self.pp.cont)
        except Exception as e:
            logger.error(f"failed to click continue button: {str(e)}")

    def choose_upi(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.upi))
            self.js_click(self.pp.upi)
        except Exception as e:
            logger.error(f"failed to click upi option: {str(e)}")

    def send_upiId(self, upiId):
        try:
            self.wait.until(EC.visibility_of_element_located(self.pp.email))
            self.send_keys(self.pp.email, str(upiId))
        except Exception as e:
            logger.error(f"failed to enter UPI ID: {str(e)}")

    def click_verify(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pp.verify))
            self.js_click(self.pp.verify)
        except Exception as e:
            logger.error(f"failed to click verify button: {str(e)}")

    def get_success_txt(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            logger.error(f"Already on main page: {str(e)}")
        try:
            longwait = WebDriverWait(self.driver, 30)
            longwait.until(EC.visibility_of_element_located(self.pp.succ))
            return self.get_text(self.pp.succ)
        except Exception as e:
            logger.error(f"Success message not found on page: {str(e)}")

    def get_pay_error_txt(self):
        try:
            return self.get_text(self.pp.payError)
        except TimeoutException:
            page_source = self.driver.page_source
            if "Amount Should Not Be Greater Than Balance" in page_source:
                return "Amount Should Not Be Greater Than Balance"
            if "Invalid Amount" in page_source:
                return "Invalid Amount."
            return ""