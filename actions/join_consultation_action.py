from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from actions.base_action import BaseAction
from pages.join_consultation_page import JoinConsultationPage
from pages.sidebar_page import SideBarPage
from utilities.logger import get_logger


class JoinConsultationAction(BaseAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.jp = JoinConsultationPage()
        self.sp = SideBarPage()
        self.logger = get_logger()

    def click_live_consultation_dropdown(self):
        self.logger.info("Clicking live consultation dropdown")
        self.js_click(self.sp.live_consultation)

    def click_live_consultation_option(self):
        self.logger.info("Clicking live consultation option")
        self.js_click(self.sp.live_consultation_option)

    def find_record_with_status(self, status_name):
        status_count = len(self.get_elements(self.jp.table_body))

        for i in range(1, status_count + 1):
            dropdown = Select(
                self.get_element(
                    self.jp.get_status_dropdown(i)
                )
            )

            status = dropdown.first_selected_option.text

            if status == status_name:
                return i

        return -1

    def find_record_not_with_status(self, status_name):
        status_count = len(self.get_elements(self.jp.table_body))

        for i in range(1, status_count + 1):
            dropdown = Select(
                self.get_element(
                    self.jp.get_status_dropdown(i)
                )
            )

            status = dropdown.first_selected_option.text

            if status != status_name:
                return i

        return -1

    def is_action_present(self, index):
        if index == -1:
            return True

        return len(
            self.get_elements(
                self.jp.get_action_buttons(index)
            )
        ) == 2

    def is_action_not_present(self, index):
        if index == -1:
            return True

        return len(
            self.get_elements(
                self.jp.get_action_buttons(index)
            )
        ) == 1

    def click_join_button(self, index):
        self.logger.info("Clicking join button")

        self.js_click(
            self.get_elements(
                self.jp.get_action_buttons(index)
            )[0]
        )

    def is_popup_displayed(self):
        return self.is_displayed(self.jp.popup)

    def is_start_now_button_displayed(self):
        return self.is_displayed(self.jp.start_now)

    def click_start_now_button(self):
        self.logger.info("Clicking Start Now button")
        self.click(self.jp.start_now)

    def is_new_browser_opened(self):
        return len(self.driver.window_handles) > 1

    def is_url_contains(self, expected_text):
        for tab in self.driver.window_handles:
            self.driver.switch_to.window(tab)

            if expected_text in self.driver.current_url:
                return True

        return False

    def click_add_button(self):
        self.logger.info("Clicking Add button")
        self.click(self.jp.add_button)

    def set_patient(self, patient):
        self.logger.info("Setting patient")

        actions = ActionChains(self.driver)

        dropdown = self.get_element(
            self.jp.patient_name
        )

        actions.move_to_element(dropdown)\
            .click()\
            .perform()

        self.send_keys_and_enter(
            self.jp.patient_name_input,
            patient
        )

        option = self.get_element(
            self.jp.first_patient_option
        )

        actions.move_to_element(option)\
            .click()\
            .perform()

    def click_add_credential_button(self):
        self.click(self.jp.add_credential_button)

    def enter_zoom_api_key(self, api_key):
        self.send_keys(
            self.jp.zoom_api_key_field,
            api_key
        )

    def enter_zoom_api_secret(self, api_secret):
        self.send_keys(
            self.jp.zoom_api_secret_field,
            api_secret
        )

    def click_save_credential_button(self):
        self.click(
            self.jp.save_credential_button
        )

    def get_toast_message(self):
        return self.get_text(
            self.jp.success_toast_message
        )

    def get_zoom_api_key_value(self):
        return self.get_element(
            self.jp.zoom_api_key_field
        ).get_attribute("value")

    def get_zoom_api_secret_value(self):
        return self.get_element(
            self.jp.zoom_api_secret_field
        ).get_attribute("value")

    def clear_credential_fields(self):
        api_key = self.get_element(
            self.jp.zoom_api_key_field
        )

        api_secret = self.get_element(
            self.jp.zoom_api_secret_field
        )

        api_key.send_keys(Keys.CONTROL, "a")
        api_key.send_keys(Keys.DELETE)

        api_secret.send_keys(Keys.CONTROL, "a")
        api_secret.send_keys(Keys.DELETE)

    def click_save_button(self):
        self.click(
            self.jp.save_consultation_button
        )