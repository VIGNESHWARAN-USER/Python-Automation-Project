from selenium.webdriver.common.by import By
class Chatpage:
    recbtn = (By.XPATH, "//a[normalize-space()='Receptionist']")
    signin = (By.XPATH, "//button[@type='submit']")
    appbtn = (By.XPATH, "//span[normalize-space()='Appointment']")
    chatbtn = (By.XPATH, "//i[@class='fa fa-whatsapp']")
    person = (By.XPATH, "//p[contains(text(),'Super Admin')]")
    msg = (By.XPATH, "//input[@placeholder='Write Your Message...']")
    sendmsg = (By.XPATH, "//i[@class='fa fa-paper-plane']")
    check = (By.XPATH, "//p[@class='name'][contains(text(),'Super Admin')]")
