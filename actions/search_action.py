from actions.base_action import BaseAction
import pages.home_page as hp
import pages.search_page as sp

class SearchAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.sp = sp.SearchPage()
        self.hp = hp.HomePage()

    def get_error_message(self):
            return self.get_text(self.sp.error_message)    

    def check_if_product_found(self, product_name):
        return self.is_displayed(self.sp.get_product_locator(product_name))

    def check_error_message(self, message):
        return self.get_error_message() == message

    def search(self, key):
        self.send_keys(self.hp.search_input, key)
        self.click(self.hp.search_button) 

    