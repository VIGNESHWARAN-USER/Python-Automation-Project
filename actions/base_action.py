from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def clear(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_attribute(self, locator, attribute):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute(attribute)

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def is_enabled(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    def is_selected(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_selected()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())

 
    def js_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def select_by_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_value(value)

    def select_by_index(self, locator, index):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_index(index)

    def hover(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        ActionChains(self.driver).drag_and_drop(source, target).perform()


    def accept_alert(self):
        self.wait.until(EC.alert_is_present()).accept()

    def dismiss_alert(self):
        self.wait.until(EC.alert_is_present()).dismiss()

    def get_alert_text(self):
        return self.wait.until(EC.alert_is_present()).text

    def send_alert_text(self, text):
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def close_current_window(self):
        self.driver.close()

    def take_screenshot(self, filename):
        self.driver.save_screenshot(f"./screenshots/{filename}.png")

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_elements_count(self, locator):
        return len(self.driver.find_elements(*locator))
