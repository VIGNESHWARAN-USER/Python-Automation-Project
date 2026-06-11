from selenium.webdriver.common.by import By


class OPDPage:

    def __init__(self, driver):
        self.driver = driver

    # Search
    opd_button = (By.XPATH,"//ul[@class='sidebar-menu verttop']/li[5]/child::a")
    old_opd_tab = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/li[3]/child::*")
    search_box = (By.XPATH,"//div[@id='DataTables_Table_1_filter']/label/input")
    patient_name = (By.XPATH,"//table[@id='DataTables_Table_1']/tbody/tr[1]/td[text()='Maria Taylor']")
    search_failed = (By.XPATH,"//td[@class='dataTables_empty']")

    # Report Download
    opd_out_patient_nav_link = (By.XPATH,"//table[@id='DataTables_Table_1']/tbody/tr[1]/td[1]/child::a")
    visits_tab = (By.XPATH,"//ul[@class='nav nav-tabs border-0 navlistscroll']/li[2]/child::a")
    print_icon = (By.XPATH,"//a[contains(@class,'buttons-pdf') and @aria-controls='DataTables_Table_1']")

    # Add Patient
    add_patient_button = (By.XPATH,"//div[@id='tab_2']/child::div/a")
    add_icon = (By.XPATH,"//div[@id='myModal']/child::div/div/div/div/div/a")
    name_field = (By.ID,"name")
    gender_dropdown = (By.ID,"addformgender")
    year_field = (By.ID,"age_year")
    month_field = (By.ID,"age_month")
    day_field = (By.ID,"age_day")
    save_button = (By.CSS_SELECTOR,"div.pull-right button#formaddpabtn")
    success_message = (By.CSS_SELECTOR,"div#toast-container div.toast-success")
    name_error_message = (By.CSS_SELECTOR,"div#toast-container div.toast-error")

    # Discharge
    revert = (By.XPATH,"//div[@class='editviewdelete-icon pt8 text-center']/child::a[4]")
    discharge_icon = (By.XPATH,"//div[@class='pull-right']/div/child::a[3]")
    date_field = (By.XPATH,"//form[@id='patient_discharge']/child::div[2]/child::div[1]/child::*/child::input")
    reason_dropdown = (By.XPATH,"//form[@id='patient_discharge']/child::div[2]/child::div[2]/child::*/child::select")
    note_field = (By.ID,"note")
    operation_field = (By.ID,"operation")
    diagnosis_field = (By.ID,"diagnosis")
    investigation_field = (By.ID,"investigations")
    save_discharge_button = (By.XPATH,"//div[@class='pull-right']/button[@id='add_paymentbtn']")