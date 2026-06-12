from selenium.webdriver.common.by import By

class SideBarPage:

    pathlogyMenu = (By.XPATH, "//a[normalize-space()='Pathology']")
    messaging = (By.xpath,"//a[@href=\"https://demo.smart-hospital.in/admin/notification\"]/child::span");