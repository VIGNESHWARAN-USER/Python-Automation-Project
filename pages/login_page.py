from selenium.webdriver.common.by import By

class LoginPage:
    email_input = (By.XPATH, "//input[@id = \"email\"]")
    password_input = (By.XPATH, "//input[@id = \"password\"]")
    sign_in_button = (By.XPATH, "//button[@type = \"submit\"]")
    super_admin = (By.XPATH, "//a[text() = \"Super Admin\"]")
    admin = (By.XPATH, "//a[text() = \"Admin\"]")
    doctor = (By.XPATH, "//a[text() = \"Doctor\"]")
    pharmacist = (By.XPATH, "//a[text() = \"Pharmacist\"]")
    pathologist = (By.XPATH, "//a[normalize-space()='Pathologist'] | //button[normalize-space()='Pathologist']")
    radiologist = (By.XPATH, "//a[text() = \"Radiologist\"]")
    accountant = (By.XPATH, "//a[text() = \"Accountant\"]")
    receptionist = (By.XPATH, "//a[text() = \"Receptionist\"]")
    nurse = (By.XPATH, "//a[text() = \"Nurse\"]")
    username_error_message = (By.XPATH, "//input[@name='username']/parent::div/descendant::p")
    password_error_message = (By.XPATH, "//input[@name='password']/parent::div/descendant::p")
    invalid_error_message = (By.XPATH, "//div[@class = \"alert alert-danger\"]")