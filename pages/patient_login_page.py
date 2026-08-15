from selenium.webdriver.common.by import By

class PatientLoginPage:

    login = (By.XPATH, "//a[text()='Login']")
    userlog = (By.XPATH, "//a[@href='https://demo.smart-hospital.in/site/userlogin']")
    signup = (By.CSS_SELECTOR, "button[type='submit']")