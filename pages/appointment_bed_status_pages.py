from selenium.webdriver.common.by import By

class Bedstatus:
    appointmentbtn = (By.XPATH,"//span[normalize-space()='Appointment']")
    bedlogo = (By.XPATH,"//a[@id='beddata']/child::i")
    patient = (By.XPATH,"(//div[contains(@class,'bedred')]/ancestor::a)[1]")
    patientdetails = (By.XPATH,"//div[@class='tab-content']")