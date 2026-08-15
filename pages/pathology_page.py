from selenium.webdriver.common.by import By

class PathalogyPage:
    
    pathlogyMenu = (By.XPATH, "//li[@class]/a[normalize-space()='Pathology']")
    search = (By.XPATH, "//div/*/input[@type='search' or @placeholder='Search...']")
    filter = (By.XPATH, "//div[text()='Records: 1 to 1 of 1 (filtered from 14 total records)']")
    table = (By.XPATH, "//table/tbody/tr")
    notFound = (By.XPATH, "//tr[@class='odd']//td[text()='No matching records found']")

    paybtn = (By.XPATH, "//table/tbody/tr/td/div/button[@type='button']")
    payAmt = (By.XPATH, "//input[@id='amount_total_paid']")
    add = (By.XPATH, "//div[@class='modal-footer']//button[@id='pay_button']")
    makepay = (By.XPATH, "//button[normalize-space()='Make Payment']")
    mobile = (By.XPATH, "//input[@type='tel']")
    cont = (By.XPATH, "//div[@class='bg-surface p-4 d:mt-2 d:px-0 px-0']//button[@type='button']")
    upi = (By.XPATH, "//*[self::a or self::li or self::div or self::span][normalize-space()='UPI']")
    email = (By.XPATH, "//input[contains(@placeholder,'upi') or contains(@placeholder,'UPI') or contains(@placeholder,'okhdfcbank') or contains(@placeholder,'@')]")
    verify = (By.XPATH, "//button[contains(normalize-space(),'Verify') or contains(normalize-space(),'Pay') or contains(normalize-space(),'verify')]")
    succ = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    payError = (By.XPATH, "//*[contains(text(),'Amount Should Not Be Greater Than Balance')] | " + "//*[contains(text(),'Invalid Amount')]")
    frame = (By.TAG_NAME,"iframe")

    def get_record_locator(self, billNo):
        xpath = f"//tr/td[contains(text(), '{billNo}')]"
        return (By.XPATH, xpath)
    
    def get_error_msg(self):
        return self.notFound