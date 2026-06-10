from selenium.webdriver.support.ui import Select
from pages.add_visitor_frontOfficePages import AddVisitor
from actions.base_action import BaseAction


class AddvisiorActions(AddVisitor):
    def __init__(self, driver):
        self.driver = driver
        
    def clk_recpbtn(self):
        self.driver.find_element(*self.recpbtn).click()
        #self.click(self.avp.recpbtn)
    def clk_signin(self):
        self.driver.find_element(*self.signinbtn).click()
        #self.click(self.avp.signinbtn)
    def clck_frontofc(self):
        self.driver.find_element(*self.frontoffice).click()
        self.driver.find_element(*self.addvisitorbtn).click()
    def add_inp(self, name, phone, idcard, noofperson, note):
        element = self.driver.find_element(*self.purpose)
        print("Displayed =", element.is_displayed())
        print("Enabled =", element.is_enabled())
        print("Tag =", element.tag_name)
        Select(self.driver.find_element(*self.purpose)).select_by_visible_text("Visit")
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.phone).send_keys(phone)
        self.driver.find_element(*self.idcard).send_keys(idcard)
        self.driver.find_element(*self.noofperson).send_keys(noofperson)
        self.driver.find_element(*self.note).send_keys(note)
    def clk_savebtn(self):
        self.driver.find_element(*self.savebtn).click()
    def check_list(self):
        return self.driver.find_element(*self.visitorlist).is_displayed()