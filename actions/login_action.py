from actions.base_action import BaseAction
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utilities.logger import get_logger

logger = get_logger()


class LoginAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.lp = LoginPage()
        self.dp = DashboardPage()

    def set_username(self, username):
        try:
            logger.info("entering username")
            self.send_keys(self.lp.email_input, username)
        except Exception as e:
            logger.error(f"Failed to enter username: {str(e)}")
            raise

    def set_password(self, password):
        try:
            logger.info("entering password")
            self.send_keys(self.lp.password_input, password)
        except Exception as e:
            logger.error(f"Failed to enter password: {str(e)}")
            raise

    def click_login_button(self):
        try:
            logger.info("clicking login button")
            self.click(self.lp.sign_in_button)
        except Exception as e:
            logger.error(f"Failed to click login button: {str(e)}")
            raise

    def get_invalid_error_message(self):
        try:
            logger.info("getting invalid message")
            return self.get_text(self.lp.invalid_error_message)
        except Exception as e:
            logger.error(f"Failed to get invalid error message: {str(e)}")
            raise

    def get_username_error_message(self):
        try:
            logger.info("username error message")
            return self.get_text(self.lp.username_error_message)
        except Exception as e:
            logger.error(f"Failed to get username error message: {str(e)}")
            raise

    def get_password_error_message(self):
        try:
            logger.info("password error message")
            return self.get_text(self.lp.password_error_message)
        except Exception as e:
            logger.error(f"Failed to get password error message: {str(e)}")
            raise

    def click_login(self, role):
        try:
            role_map = {
                "Super Admin": self.lp.super_admin,
                "Admin": self.lp.admin,
                "Doctor": self.lp.doctor,
                "Nurse": self.lp.nurse,
                "Pharmacist": self.lp.pharmacist,
                "Pathologist": self.lp.pathologist,
                "Radiologist": self.lp.radiologist,
                "Accountant": self.lp.accountant,
                "Receptionist": self.lp.receptionist
            }

            if role not in role_map:
                raise ValueError(f"Invalid role: {role}")

            logger.info(f"clicking {role}")
            self.click(role_map[role])

        except Exception as e:
            logger.error(f"Failed to click login role: {role} - {str(e)}")
            raise

    def get_user_role(self):
        try:
            self.click(self.dp.profile_icon)
            return self.get_text(self.dp.role)
        except Exception as e:
            logger.error(f"Failed to get user role: {str(e)}")
            raise

    def is_correct_user_logged_in(self, role):
        return self.get_user_role() == role

    def is_correct_error_message_displayed(self, message):
        return self.get_invalid_error_message() == message

    def is_username_error_message_displayed(self, message):
        return message == self.get_username_error_message()

    def is_password_error_message_displayed(self, message):
            return message == self.get_password_error_message()

    def is_validation_error_messages_displayed(self, messages):
        for message in messages:
            if message not in [self.get_password_error_message() ,self.get_username_error_message()]:
                return False
        return True
    
