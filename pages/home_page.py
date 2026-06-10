from selenium.webdriver.common.by import By

class HomePage:
    my_account_icon = (By.XPATH, "//i[@class = \"fa fa-user\"]")
    login_button = (By.LINK_TEXT, "Login")
    search_input = (By.XPATH, "//input[@name = 'search']")
    search_button = (By.XPATH, "//i[@class = \"fa fa-search\"]")
    