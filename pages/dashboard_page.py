from selenium.webdriver.common.by import By

class DashboardPage:
    profile_icon = (By.XPATH, "//div[@class=\"tb-signet-text\"]")
    role = (By.XPATH, "//div[@class=\"text-muted small\"]")