from selenium.webdriver.common.by import By

class AddVisitor:
    recpbtn = (By.XPATH,"//a[normalize-space()='Receptionist']")
    signinbtn = (By.XPATH,"//button[@type='submit']")
    frontoffice = (By.XPATH,"//span[normalize-space()='Front Office']")
    addvisitorbtn = (By.XPATH,"//a[@class='btn btn-primary btn-sm addvisitor']")
    purpose = (By.XPATH,"//form[@id='formadd']//select[@name='purpose']")
    name = (By.XPATH,"//form[@id='formadd']//input[@name='name']")
    phone = (By.XPATH,"//form[@id='formadd']//input[@name='contact']")
    idcard = (By.XPATH,"//form[@id='formadd']//input[@name='id_proof']")
    noofperson = (By.XPATH,"//input[@fdprocessedid='qrrtqp']")
    note = (By.XPATH,"//textarea[@id='description']")
    savebtn = (By.XPATH,"//button[@id='formaddbtn']")
    visitorlist = (By.XPATH,"//h3[text()='Visitor List']/parent::div") 