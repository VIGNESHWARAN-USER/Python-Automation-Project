from actions.base_action import BaseAction
import pages.home_page as hp
import pages.login_page as lp

class LoginAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.lp = lp.LoginPage()
        self.hp = hp.HomePage()

    def set_email(self, email):
        self.send_keys(self.lp.email_input, email)

    def set_password(self, password):
        self.send_keys(self.lp.password_input, password)

    def click_login_button(self):
         self.click(self.lp.login_button)

    def click_my_account_icon(self):
        self.click(self.hp.my_account_icon)

    def click_login_option(self):
        self.click(self.hp.login_button)

    def get_error_message(self):
        return self.get_text(self.lp.error_message)

    def check_if_logged_in(self):
        return "account" in self.driver.current_url.lower()

    def check_error_message(self, message):
        return self.get_error_message() == message

    def login(self, email, password):
        self.click_my_account_icon()
        self.click_login_option()
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()    

    