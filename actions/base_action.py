from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from datetime import datetime
import os
import time


class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Click Actions
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator):
        # element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, locator[1]))

    def scroll_and_click(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();")
        self.click(locator)

    # Text Actions
    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def send_keys_and_enter(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(value)
        element.send_keys(Keys.ENTER)


    def clear(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # Validation
    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_enabled(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    def is_selected(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_selected()

    # Dropdown
    def select_by_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_value(value)

    def select_by_index(self, locator, index):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_index(index)

    # Waits
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Browser
    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    # Screenshot
    def take_screenshot(self, filename):

        screenshot_dir = "./screenshots"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filepath = f"{screenshot_dir}/" f"{filename}_{timestamp}.png"

        self.driver.save_screenshot(filepath)

        return filepath

    # Mouse Actions
    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))

        ActionChains(self.driver).context_click(element).perform()

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
