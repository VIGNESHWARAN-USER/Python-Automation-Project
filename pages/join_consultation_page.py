from selenium.webdriver.common.by import By

class JoinConsultationPage:
    tableBody = (By.XPATH, "//div/table/tbody/tr")
    popUp = (By.XPATH, "//div[@id = \"modal-chkstatus\"]")
    startNow = (By.XPATH, "//a[contains(@href , \"zoom\") and @class = \"btn btn-outline-success btn-sm pull-right\"]")
    addButton = (By.XPATH, "//div[@class = \"box-tools pull-right box-tools-md\"]/button[1]")
    patientName = (By.XPATH, "//select[@id = \"addpatient_id\"]/following-sibling::span/span/span/span[2]")
    firstPatientoption = (By.XPATH, "//span[@class = \"select2-results\"]/ul/li[1]")
    patientNameInput =(By.CSS_SELECTOR, "input.select2-search__field")
    title = (By.XPATH, "//input[@name = \"title\"]")
    date = (By.CSS_SELECTOR, "input#datetimepicker")
    duration = (By.CSS_SELECTOR, "input#duration")
    ipdOrOpd = (By.XPATH, "//select[@class = \"form-control module_type\"]")
    description = (By.CSS_SELECTOR, "textarea#description")
    addCredentialButton = (By.XPATH, "//div[@class= \"box-tools pull-right box-tools-md\"]/button[2]")
    zoomApiKeyField = (By.XPATH, "//input[@id = \"zoom_api_key\"]")
    zoomApiSecretField = (By.XPATH, "//input[@id = \"zoom_api_secret\"]")
    saveCredentialButton = (By.XPATH, "//button[@id = \"submit-btn-credential\"][2]")
    successToastMessage = (By.XPATH, "//div[@class = \"toast-message\"]")
    saveConsultationButton = (By.XPATH, "//div[@class = \"pull-right mrminus8\"]/button[@class = \"btn btn-primary\"]")


    def getStatusDropdown(self, rowIndex):
        return (By.XPATH, "//tbody/tr[" + rowIndex + "]/td[8]/form/select")
    

    def getActionButtons(self, rowIndex):
        return (By.XPATH, "//tbody/tr[" + rowIndex + "]/td[9]/a")
    