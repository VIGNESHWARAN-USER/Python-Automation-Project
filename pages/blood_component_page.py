from selenium.webdriver.common.by import By

class BloodComponentPage:

    billing = (By.XPATH, "//span[text()=' Billing']")
    bloodcomp = (By.XPATH, "//p[text()='Blood Component Issue']")
    details = (By.XPATH, "(//a[i[@class='fa fa-reorder']])[1]")
    patientpopup = (By.XPATH, "//h4[text()='Blood Component Issue Details']")