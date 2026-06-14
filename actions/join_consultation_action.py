from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.config_reader import get_value
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
        try:
            self.logger.info("Clicking live consultation dropdown")
            self.js_click(self.sp.live_consultation)
        except Exception as e:
            self.logger.error(f"Failed to click live consultation dropdown: {str(e)}")
            raise

    def click_live_consultation_option(self):
        try:
            self.logger.info("Clicking live consultation option")
            self.js_click(self.sp.live_consultation_option)
        except Exception as e:
            self.logger.error(f"Failed to click live consultation option: {str(e)}")
            raise

    def click_join_button(self, index):
        try:
            self.logger.info("Clicking join button")
            self.js_click(
                self.get_elements(
                    self.jp.get_action_buttons(index)
                )[0]
            )
        except Exception as e:
            self.logger.error(f"Failed to click join button: {str(e)}")
            raise

    def click_start_now_button(self):
        try:
            self.logger.info("Clicking Start Now button")
            self.click(self.jp.start_now)
        except Exception as e:
            self.logger.error(f"Failed to click Start Now button: {str(e)}")
            raise

    def click_add_button(self):
        try:
            self.logger.info("Clicking Add button")
            self.click(self.jp.add_button)
        except Exception as e:
            self.logger.error(f"Failed to click Add button: {str(e)}")
            raise

    def set_patient(self, patient):
        try:
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

        except Exception as e:
            self.logger.error(f"Failed to set patient: {str(e)}")
            raise

    def click_add_credential_button(self):
        try:
            self.logger.info("Clicking Add Credential button")
            self.click(self.jp.add_credential_button)
        except Exception as e:
            self.logger.error(f"Failed to click Add Credential button: {str(e)}")
            raise

    def enter_zoom_api_key(self, api_key):
        try:
            self.logger.info("Entering Zoom API Key")
            self.send_keys(
                self.jp.zoom_api_key_field,
                api_key
            )
        except Exception as e:
            self.logger.error(f"Failed to enter Zoom API Key: {str(e)}")
            raise

    def enter_zoom_api_secret(self, api_secret):
        try:
            self.logger.info("Entering Zoom API Secret")
            self.send_keys(
                self.jp.zoom_api_secret_field,
                api_secret
            )
        except Exception as e:
            self.logger.error(f"Failed to enter Zoom API Secret: {str(e)}")
            raise

    def click_save_credential_button(self):
        try:
            self.logger.info("Clicking Save Credential button")
            self.click(
                self.jp.save_credential_button
            )
        except Exception as e:
            self.logger.error(f"Failed to click Save Credential button: {str(e)}")
            raise

    def get_toast_message(self):
        try:
            self.logger.info("Getting toast message")
            return self.get_text(
                self.jp.success_toast_message
            )
        except Exception as e:
            self.logger.error(f"Failed to get toast message: {str(e)}")
            raise

    def get_zoom_api_key_value(self):
        try:
            self.logger.info("Getting Zoom API Key value")
            return self.get_element(
                self.jp.zoom_api_key_field
            ).get_attribute("value")
        except Exception as e:
            self.logger.error(f"Failed to get Zoom API Key value: {str(e)}")
            raise

    def get_zoom_api_secret_value(self):
        try:
            self.logger.info("Getting Zoom API Secret value")
            return self.get_element(
                self.jp.zoom_api_secret_field
            ).get_attribute("value")
        except Exception as e:
            self.logger.error(f"Failed to get Zoom API Secret value: {str(e)}")
            raise

    def clear_credential_fields(self):
        try:
            self.logger.info("Clearing credential fields")

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

        except Exception as e:
            self.logger.error(f"Failed to clear credential fields: {str(e)}")
            raise

    def click_save_button(self):
        try:
            self.logger.info("Clicking Save button")
            self.click(
                self.jp.save_consultation_button
            )
        except Exception as e:
            self.logger.error(f"Failed to click Save button: {str(e)}")
            raise

    def find_record_with_status(self, status_name):
            try:
                self.logger.info(f"Finding record with status: {status_name}")
    
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
    
            except Exception as e:
                self.logger.error(f"Failed to find record with status '{status_name}': {str(e)}")
                raise
    
    
    def find_record_not_with_status(self, status_name):
        try:
            self.logger.info(f"Finding record not having status: {status_name}")

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

        except Exception as e:
            self.logger.error(f"Failed to find record not having status '{status_name}': {str(e)}")
            raise


    def is_action_present(self, index):
        try:
            self.logger.info(f"Checking whether action is present for row {index}")

            if index == -1:
                return True

            return len(
                self.get_elements(
                    self.jp.get_action_buttons(index)
                )
            ) == 2

        except Exception as e:
            self.logger.error(f"Failed to verify action presence for row {index}: {str(e)}")
            raise


    def is_action_not_present(self, index):
        try:
            self.logger.info(f"Checking whether action is not present for row {index}")

            if index == -1:
                return True

            return len(
                self.get_elements(
                    self.jp.get_action_buttons(index)
                )
            ) == 1

        except Exception as e:
            self.logger.error(f"Failed to verify action absence for row {index}: {str(e)}")
            raise


    def is_popup_displayed(self):
        try:
            self.logger.info("Checking whether popup is displayed")
            return self.is_displayed(self.jp.popup)

        except Exception as e:
            self.logger.error(f"Failed to verify popup display: {str(e)}")
            raise


    def is_start_now_button_displayed(self):
        try:
            self.logger.info("Checking whether Start Now button is displayed")
            return self.is_displayed(self.jp.start_now)

        except Exception as e:
            self.logger.error(f"Failed to verify Start Now button display: {str(e)}")
            raise


    def is_new_browser_opened(self):
        try:
            self.logger.info("Checking whether a new browser window is opened")
            return len(self.driver.window_handles) > 1

        except Exception as e:
            self.logger.error(f"Failed to verify new browser window: {str(e)}")
            raise


    def is_url_contains(self, expected_text):
        try:
            self.logger.info(f"Verifying URL contains: {expected_text}")

            for tab in self.driver.window_handles:
                self.driver.switch_to.window(tab)

                if expected_text in self.driver.current_url:
                    return True

            return False

        except Exception as e:
            self.logger.error(f"Failed to verify URL contains '{expected_text}': {str(e)}")
            raise


    def is_credentials_added(self):
        try:
            self.logger.info("Verifying credentials were added successfully")
            print(get_value(
                                "./data_files/consultation_data.ini",
                                "data set",
                                "success_message"
                            ))
            print(self.get_toast_message())
            return (
                get_value(
                    "./data_files/consultation_data.ini",
                    "data set",
                    "success_message"
                )
                == self.get_toast_message()
            )

        except Exception as e:
            self.logger.error(f"Failed to verify credentials addition: {str(e)}")
            raise   


    def is_action_clickable(self, index):
        try:
            action_button = self.get_elements(
                self.jp.get_action_buttons(index)
            )[0]

            return self.is_clickable(action_button)

        except Exception as e:
            self.logger.error(
                f"Failed to verify action clickable: {str(e)}"
            )
            raise