from selenium.webdriver.common.by import By

class LoginPage:
    email_input = (By.XPATH, "//input[@id=\"al-username\"]")
    password_input = (By.XPATH, "//input[@id=\"al-password\"]")
    sign_in_button = (By.XPATH, "//button[@type = \"submit\"]")
    super_admin = (By.XPATH, "//button[text() = \"Super Admin\"]")
    admin = (By.XPATH, "//button[text() = \"Admin\"]")
    doctor = (By.XPATH, "//button[text() = \"Doctor\"]")
    pharmacist = (By.XPATH, "//button[text() = \"Pharmacist\"]")
    pathologist = (By.XPATH, "//button[text() = \"Pathologist\"]")
    radiologist = (By.XPATH, "//button[text() = \"Radiologist\"]")
    accountant = (By.XPATH, "//button[text() = \"Accountant\"]")
    receptionist = (By.XPATH, "//button[text() = \"Receptionist\"]")
    nurse = (By.XPATH, "//button[text() = \"Nurse\"]")
    username_error_message = (By.XPATH, "//input[@name='username']/parent::div/descendant::p")
    password_error_message = (By.XPATH, "//input[@name='password']/parent::div/descendant::p")
    invalid_error_message = (By.XPATH, "//div[@class=\"alert alert-danger mt-3\"]")