from selenium.webdriver.common.by import By

class SideBarPage:
    liveConsultation = (By.XPATH, "//li[contains(@class ,\"treeview\")][19]")
    liveConsultationOption = (By.XPATH, "//li[contains(@class ,\"treeview\")][19]/ul/li/a")
    pathlogyMenu = (By.XPATH, "//a[normalize-space()='Pathology']")
    messaging = (By.XPATH,"//a[@href=\"https://demo.smart-hospital.in/admin/notification\"]/child::span");