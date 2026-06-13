from selenium.webdriver.common.by import By

class SendMsg:

    sendSms = (By.XPATH,"//a[@href=\"https://demo.smart-hospital.in/admin/notification/add\"]/following-sibling::a")
    title = (By.XPATH,"(//div[@class='form-group']/child::input)[1]")
    tempId = (By.XPATH,"(//label[text()='Template Id']/following-sibling::input)[1]")
    sms = (By.XPATH,"(//label[@class='checkbox-inline']/child::input)[1]")
    mobileApp = (By.XPATH,"(//label[@class='checkbox-inline']/input[@value='push'])[1]")
    message  = (By.XPATH,"//label[text()='Message']/following-sibling::textarea[@name='group_message']")
    dtr = (By.XPATH,"//input[@value='3']");
    nurse = (By.XPATH,"//input[@value='9']");
    send = (By.XPATH,"(//div[@class='pull-right']/child::button)[1]")
    succMsg = (By.XPATH,"//div[text()='Record Saved Successfully']")
    emptyError = (By.XPATH,"//div[@class='toast-message']//p[text()='Message To field is required']")
    missingFieldError = (By.XPATH,"//div[@class='toast-message']//p[text()='Send Through field is required']")
    
    def get_success_msg(self):
        return self.succMsg
    
    def get_error_msg(self):
        return self.emptyError
    
    def get_missing_msg(self):
        return self.missingFieldError