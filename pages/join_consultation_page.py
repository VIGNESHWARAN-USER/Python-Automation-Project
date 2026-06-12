from selenium.webdriver.common.by import By

class JoinConsultationPage:
    table_body = (By.XPATH, "//div/table/tbody/tr")
    popup = (By.XPATH, "//div[@id = 'modal-chkstatus']")
    start_now = (By.XPATH,"//a[contains(@href , 'zoom') and @class = 'btn btn-outline-success btn-sm pull-right']")
    add_button = (By.XPATH,"//div[@class = 'box-tools pull-right box-tools-md']/button[1]")
    patient_name = (By.XPATH,"//select[@id = 'addpatient_id']/following-sibling::span/span/span/span[2]")
    first_patient_option = (By.XPATH,"//span[@class = 'select2-results']/ul/li[1]")
    patient_name_input = (By.CSS_SELECTOR,"input.select2-search__field")
    title = (By.XPATH,"//input[@name = 'title']")
    date = (By.CSS_SELECTOR,"input#datetimepicker")
    duration = (By.CSS_SELECTOR,"input#duration")
    ipd_or_opd = (By.XPATH,"//select[@class = 'form-control module_type']")
    description = (By.CSS_SELECTOR,"textarea#description")
    add_credential_button = (By.XPATH,"//div[@class = 'box-tools pull-right box-tools-md']/button[2]")
    zoom_api_key_field = (By.XPATH,"//input[@id = 'zoom_api_key']")
    zoom_api_secret_field = (By.XPATH,"//input[@id = 'zoom_api_secret']")
    save_credential_button = (By.XPATH,"//button[@id = 'submit-btn-credential'][2]")
    success_toast_message = (By.XPATH,"//div[@class = 'toast-message']")
    save_consultation_button = (By.XPATH,"//div[@class = 'pull-right mrminus8']/button[@class = 'btn btn-primary']")

    def get_status_dropdown(self, rowIndex):
        return (By.XPATH, "//tbody/tr[" + rowIndex + "]/td[8]/form/select")
    

    def get_action_buttons(self, rowIndex):
        return (By.XPATH, "//tbody/tr[" + rowIndex + "]/td[9]/a")
    