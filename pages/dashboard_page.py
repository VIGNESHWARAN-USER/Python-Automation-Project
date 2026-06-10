from selenium.webdriver.common.by import By

class DashboardPage:
    profile_icon = (By.XPATH, "//img[@class = \"topuser-image\"]")
    role = (By.XPATH, "//div[@class = \"sstopuser-test\"]/h5")