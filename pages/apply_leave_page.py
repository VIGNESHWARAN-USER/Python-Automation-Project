from selenium.webdriver.common.by import By

class ApplyLeavePage:

    leaves = (By.XPATH,"//div[@class='box-tools pull-right']/a")
    applyLeave = (By.XPATH,"//small[@class='pull-right']/a[@href]")
    leaveType = (By.XPATH,"//div[@id='leavetypeddl']/select[@name]")
    sick = (By.XPATH,"//select[@name]/option[text()='Sick Leave (15)']")
    leaveFrom = (By.XPATH,"//tr/td[text()='29']")
    leaveTo = (By.XPATH,"//tr/td[text()='30']")
    reason = (By.XPATH,"//div[@class]/textarea[@name='reason']")
    savebtn = (By.XPATH,"(//div[@class='modal-footer']/button[@type='submit'])[1]")