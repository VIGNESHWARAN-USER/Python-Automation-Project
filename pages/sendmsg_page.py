from selenium.webdriver.common.by import By

class SendMsg:

    sendSms = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/mailsms/compose']")
    title = (By.XPATH,"//div/*/input[@name='group_title']")
    tempId = (By.XPATH,"//div/*/input[@name='group_template_id']")
    sms = (By.XPATH,"(//div/*/input[@value='sms'])[1]")
    mobileApp = (By.XPATH,"(//div/*/input[@value='push'])[1]")
    message  = (By.XPATH,"//div/*/textarea[@name='group_message']")
    dtr = (By.XPATH,"//div/*/input[@value='3']");
    nurse = (By.XPATH,"//div/*/input[@value='9']");
    send = (By.XPATH,"//div/button[@class='btn btn-primary submit_group']")
    succMsg = (By.XPATH,"//div[text()='Record Saved Successfully']")
    emptyError = (By.XPATH,"//div[@class='sh-bubble-msg']/p[normalize-space()='Message To field is required']")
    missingFieldError = (By.XPATH,"//div[@class='sh-bubble-msg']/p[normalize-space()='Send Through field is required']")
    
    def get_success_msg(self):
        return self.succMsg
    
    def get_error_msg(self):
        return self.emptyError
    
    def get_missing_msg(self):
        return self.missingFieldError