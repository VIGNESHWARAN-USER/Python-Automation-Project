from selenium.webdriver.common.by import By

class ApplyLeavePage:

    leaves = (By.XPATH,"//div[@class='box-tools pull-right']/a")
    applyLeave = (By.XPATH,"//small[@class='pull-right']/a[@href]")
    leaveType = (By.XPATH,"//select[@id='leave_type']")
    sick = (By.XPATH,"//select[@name]/option[text()='Sick Leave (15)']")
    leaveFrom = (By.XPATH,"//tr/td[text()='29']")
    leaveTo = (By.XPATH,"//tr/td[text()='30']")
    reason = (By.XPATH,"//div[@class]/textarea[@name='reason']")
    savebtn = (By.XPATH,"(//div[@class='modal-footer']/button[@type='submit'])[1]")
    succmsg = (By.XPATH, "//div[@class='alert alert-success']")
    missfield = (By.XPATH,"//p[text()='Leave To Date field is required']")
    emptyfield = (By.XPATH,"//div[@id]/div[@class]/div[@class='toast-message']")