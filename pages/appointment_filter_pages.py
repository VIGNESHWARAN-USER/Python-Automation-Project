from selenium.webdriver.common.by import By

class Apponintmentfilter:
    appointmentbtn = (By.XPATH,"//li//a//span[text()='Appointment']")
    todayapp = (By.XPATH,"//ul[contains(@class,'nav nav-pills sh-segmented-tabs')]//button[normalize-space()='Today Appointment']")
    todayapptable = (By.XPATH,"//div[@class='card-header d-flex align-items-center justify-content-between flex-wrap gap-2 py-0 px-3']")
    upcomingapp = (By.XPATH,"//ul[contains(@class,'nav nav-pills sh-segmented-tabs')]//button[normalize-space()='Upcoming Appointment']")
    upcomingapptable = (By.XPATH,"//div[@class='card-header d-flex align-items-center justify-content-between flex-wrap gap-2 py-0 px-3']")
    #upcomingapptable = (By.XPATH,"//table[@id='DataTables_Table_1']")
    oldapp = (By.XPATH,"//ul[contains(@class,'nav nav-pills sh-segmented-tabs')]//button[normalize-space()='Old Appointment']")
    oldapptable = (By.XPATH,"//div[@class='card-header d-flex align-items-center justify-content-between flex-wrap gap-2 py-0 px-3']")
    