
from selenium.webdriver.common.by import By

class ProfilePage:

    profile_button = (By.XPATH, "//div[@class='sspass']//a[1]")
    role           = (By.XPATH, "//div[@class='col-lg-2 col-md-4 col-sm-4 border-right'][2]/span")
    leave_button   = (By.XPATH, "//ul[@class='nav nav-tabs navlistscroll']//child::li[2]/child::a")
    leave_table    = (By.ID,    "DataTables_Table_2")