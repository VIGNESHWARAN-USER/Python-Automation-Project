from selenium.webdriver.common.by import By

class SearchPage:
    error_message = (By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]")

    def get_product_locator(self, product_name):
        xpath = "//a[text() = \""+product_name+"\"]"
        return (By.XPATH, xpath)