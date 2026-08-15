from selenium.webdriver.common.by import By

class SideBarPage:
    
    live_consultation = (By.XPATH, "//li[contains(@class ,\"treeview\")][19]")
    live_consultation_option = (By.XPATH, "//li[contains(@class ,\"treeview\")][19]/ul/li/a")
    pathlogyMenu = (By.XPATH, "//a[normalize-space()='Pathology']")
    message = (By.XPATH,"//a[@href=\"https://demo.smart-hospital.in/admin/notification\"]/child::span");
    appointmentbtn = (By.XPATH, "//ul[@class='sidebar-menu verttop']/li[@class='treeview active']/following-sibling::li[3]/child::a/child::i")
    frontoffice = (By.XPATH,"//li[contains(@class ,'treeview')][12]")
    dashboard = (By.XPATH,"//li[contains(@class ,'treeview')][1]")
    patient = (By.XPATH,"//li[contains(@class ,'treeview')][2]")
    billing = (By.XPATH,"//li[contains(@class ,'treeview')][3]")
    extraappointmentbtn = (By.XPATH,"//li[contains(@class ,'treeview')][4]")
    opdoutpatient= (By.XPATH,"//li[contains(@class ,'treeview')][5]")
    ipdinpatient = (By.XPATH,"//li[contains(@class ,'treeview')][6]")
    pharmacy = (By.XPATH,"//li[contains(@class ,'treeview')][7]")
    pathology = (By.XPATH,"//li[contains(@class ,'treeview')][8]")
    messaging = (By.XPATH,"//li[contains(@class ,'treeview')][16]")
    inventory = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/itemstock']")
    humanRes = (By.XPATH,"//a[@href=\"https://demo.smart-hospital.in/admin/staff\"]/span[text()='Human Resource']")
    bloodbank = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/bloodbankstatus/']")