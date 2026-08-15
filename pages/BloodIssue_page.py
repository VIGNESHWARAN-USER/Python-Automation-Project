from selenium.webdriver.common.by import By

class BloodIssue:
    
    profile = (By.XPATH,"//img[@class='topuser-image']")
    pathologylog = (By.XPATH,"//h5[text()='Pathologist']")
    blood = (By.XPATH,"(//a[@onclick='getBloodListTable(this.id)'])[8]")
    status = (By.XPATH,"//h3[text()='Blood Bank Status']")
    issue = (By.XPATH,"//button[@onclick='bloodIssueModal(8,1138)']")
    form = (By.XPATH,"(//div[@class='box-body'])[1]")