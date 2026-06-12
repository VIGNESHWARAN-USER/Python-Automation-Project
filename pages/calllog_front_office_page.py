from selenium.webdriver.common.by import By

class CallLogPage:
    recbtnfo=(By.CSS_SELECTOR,".btn.btn-primary.width50[href='#'][onclick=\\\"copy('maria@gmail.com', 'password')\\\"]",)
    signinfo=(By.XPATH, "//button[@type='submit']")
    frontofc=(By.XPATH,"//li//a//span[text()='Front Office'] | //span[contains(text(),'Front Office')] | //li/a/span[contains(.,'Front Office')]",)
    #phcalllog=(By.XPATH,"//div[@class = 'box-tools pull-right']//a[@href = 'https://demo.smart-hospital.in/admin/generalcall']")
    phcalllog = (By.XPATH,"//a[normalize-space()='Phone Call Log']")
    addlog=(By.XPATH, "//a[@class='btn btn-primary btn-sm call_log']")
    name=(By.XPATH, "//form[@id='formadd']//input[@name='name']")
    phone=(By.XPATH, "//form[@id='formadd']//input[@name='contact']")
    desc=(By.XPATH,"//label[text()='Description']//following-sibling::textarea[@id='description']",)
    callduration = (By.XPATH, "//form[@id='formadd']//input[@name='call_dureation']")
    note=(By.XPATH,"//label[text()='Note']//following-sibling::textarea[@id='description']",)
    incom= (By.XPATH,"//form[@id='formadd']//input[@name='call_type' and @value='Incoming']",)
    outgng =(By.XPATH,"//form[@id='formadd']//input[@name='call_type' and @value='Outgoing']",)
    savebtn= (By.XPATH, "//button[@id='formaddbtn']")
    checklist =(By.XPATH, "//h3[@class='box-title titlefix']")
    error =(By.XPATH, "//h3[@class='box-title titlefix']")