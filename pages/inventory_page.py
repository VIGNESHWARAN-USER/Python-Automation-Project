from selenium.webdriver.common.by import By

class inventory:
    itemstocklist = (By.XPATH,"//table[@id='DataTables_Table_0']/child::thead/child::tr")
    issueitem = (By.XPATH,"//div[@class='box-tools pull-right']/child::a")
    excel = (By.XPATH,"//a[@class='btn btn-default dt-button buttons-excel buttons-html5 btn-excel']/child::span/child::i")
    csv = (By.XPATH,"//a[@class='btn btn-default dt-button buttons-csv buttons-html5 btn-csv']/child::span/child::i")
    pdf = (By.XPATH,"//a[@class='btn btn-default dt-button buttons-pdf buttons-html5 btn-pdf']/child::span/child::i")
    issueitemlist = (By.XPATH,"//table[@id='DataTables_Table_0']/child::thead/child::tr")
    
    