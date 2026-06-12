from selenium.webdriver.common.by import By

class SideBarPage:

    pathlogyMenu = (By.XPATH, "//a[normalize-space()='Pathology']")
    messaging = (By.XPATH,"//a[@href=\"https://demo.smart-hospital.in/admin/notification\"]/child::span");