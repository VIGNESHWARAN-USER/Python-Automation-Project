from selenium.webdriver.common.by import By


class CertificatePage:

    certificate_menu = (By.XPATH, "//span[normalize-space()='Certificate']")
    certificate_sub_menu = (By.XPATH, "//a[contains(@href,'generatecertificate')]")
    module_dropdown = (By.ID, "module")
    patient_status_dropdown = (By.ID, "patient_status")
    certificate_template_dropdown = (By.NAME, "certificate_id")
    search_button = (By.XPATH, "//button[contains(.,'Search')]")
    generate_button = (By.XPATH, "//button[contains(@title,'generate')]")
    close_details_page = (
        By.XPATH,
        "//button[contains(text(),'Cancel') or contains(text(),'Close')]"
    )

    @staticmethod
    def get_patient_checkbox_locator(patient_name):
        return (
            By.XPATH,
            f"//tr[td[contains(normalize-space(),'{patient_name}')]]"
            f"//input[@type='checkbox']"
        )