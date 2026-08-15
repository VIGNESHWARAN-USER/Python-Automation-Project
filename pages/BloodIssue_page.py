from selenium.webdriver.common.by import By

class BloodIssue:
    
    # profile = (By.XPATH,"//img[@class='topuser-image']")
    pathologylog = (By.XPATH,"//span[@class='tb-signet-role']")
    blood = (By.XPATH,"//div[@class='bb-pill-list']/div[8]")
    status = (By.XPATH,"//div[@class='bb-card-hdr']/*[1]")
    issue = (By.XPATH,"//button[@onclick='bloodIssueModal(8,1138)']")
    form = (By.XPATH,"(//div[@class='sh-card-header'])[8]")