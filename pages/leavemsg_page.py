from selenium.webdriver.common.by import By

class LeaveMsg:

    pathologistBtn = (By.xpath,"//a[normalize-space()='Pathologist'] | //button[normalize-space()='Pathologist']")
    signInBtn = (By.xpath,"//button[normalize-space()='Sign In']")
    pathalogist = (By.xpath,"//a[@onclick=\"copy('harry@gmail.com', 'password')\"]/following-sibling::a[1]")
    sendSms = (By.xpath,"//a[@href=\"https://demo.smart-hospital.in/admin/notification/add\"]/following-sibling::a")
    title = (By.xpath,"(//div[@class='form-group']/child::input)[1]")
    tempId = (By.xpath,"(//label[text()='Template Id']/following-sibling::input)[1]")
    sms = (By.xpath,"(//label[@class='checkbox-inline']/child::input)[1]")
    mobileApp = (By.xpath,"(//label[@class='checkbox-inline']/input[@value='push'])[1]")
    message  = (By.xpath,"//label[text()='Message']/following-sibling::textarea[@name='group_message']")
    dtr = (By.xpath,"//input[@value='3']");
    nurse = (By.xpath,"//input[@value='9']");
    send = (By.xpath,"(//div[@class='pull-right']/child::button)[1]")
    succMsg = (By.xpath,"//div[text()='Record Saved Successfully']")
    emptyError = (By.xpath,"//div[@class='toast-message']//p[text()='Message To field is required']")
    missingFieldError = (By.xpath,"//div[@class='toast-message']//p[text()='Send Through field is required']")
    
    def get_success_msg(self):
        return self.succMsg
    
    def get_error_msg(self):
        return self.emptyError
    
    def get_missing_msg(self):
        return self.missingFieldError