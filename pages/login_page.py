from selenium.webdriver.common.by import By

class LoginPage:
    email_input = (By.ID, "input-email")
    password_input = (By.ID, "input-password")
    login_button = (By.XPATH,"//input[@value='Login']")
    error_message = (By.XPATH, "//div[contains(@class ,\"alert\")]")
    