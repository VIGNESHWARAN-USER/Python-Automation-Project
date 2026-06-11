from selenium.webdriver.common.by import By

class Apponintmentfilter:
    appointmentbtn = (By.XPATH,"//i[@class='fa fa-calendar-check-o']/following-sibling::span[text()='Appointment']")
    todayapp = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[1]")
    todayapptable = (By.XPATH,"//table[@id='DataTables_Table_0']")
    upcomingapp = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[2]")
    upcomingapptable = (By.XPATH,"//table[@id='DataTables_Table_1']/child::thead/child::tr/child::th[text()='Patient Name']")
    #upcomingapptable = (By.XPATH,"//table[@id='DataTables_Table_1']")
    oldapp = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[3]")
    oldapptable = (By.XPATH,"//div[@id='DataTables_Table_2_wrapper']")
    