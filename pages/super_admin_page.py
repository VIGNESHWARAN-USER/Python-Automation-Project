from selenium.webdriver.common.by import By

class superadmin:
    opd = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/patient/search']/child::span[@class='info-box-icon bg-green']")
    opdpatientview = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[4]")
    oldopd = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[3]")
    upcimopd = (By.XPATH,"//ul[@class='nav nav-tabs navlistscroll']/child::li[2]")
     
    ipd = (By.XPATH,"//div[@class='col-lg-2 col-md-3 col-sm-6 col20']/child::div/child::a[@href='https://demo.smart-hospital.in/admin/patient/ipdsearch']")
    patientlistipd = (By.XPATH,"//div[@class='table-responsive overflow-visible-lg']")
    
    pharmacy = (By.XPATH,"//div[@class='col-lg-2 col-md-3 col-sm-6 col20']/child::div/child::a[@href='https://demo.smart-hospital.in/admin/pharmacy/bill']")
    medicine = (By.XPATH,"//a[contains(@href,'/admin/pharmacy/search')] | //a[@class='btn btn-primary btn-sm addmedicine']")
    addmed = (By.XPATH,"//a[@class='btn btn-primary btn-sm addmedicine']")
    medname = (By.XPATH,"//input[@id='medicine_name']")
    medcat = (By.XPATH,"//form[@id='formadd']//select[@name='medicine_company']")
    medcompany = (By.XPATH,"//form[@id='formadd']//select[@name='medicine_company']")
    medcompos =(By.XPATH,"//form[@id='formadd']//input[@name='medicine_composition']")
    medgroup = (By.XPATH,"//form[@id='formadd']//select[@name='medicine_group']")
    unit = (By.XPATH,"//form[@id='formadd']//select[@name='unit']")
    minlvl = (By.XPATH,"//form[@id='formadd']//input[@name='min_level']")
    reorder = (By.XPATH,"//form[@id='formadd']//input[@name='reorder_level']")
    tax = (By.XPATH,"//form[@id='formadd']//input[@name='vat']")
    box = (By.XPATH,"//form[@id='formadd']//input[@name='unit_packing']")
    racknum = (By.XPATH,"//form[@id='formadd']//input[@name='rack_number']")
    vatac = (By.XPATH,"//form[@id='formadd']//input[@name='vat_ac']")
    note = (By.XPATH,"//textarea[@autocomplete='off']")
    savebtn = (By.XPATH,"//button[@id='formaddbtn']")
    medicinestock = (By.XPATH,"//h3[@class='box-title titlefix']")
    
    
    pathology = (By.XPATH,"//div[@class='col-lg-2 col-md-3 col-sm-6 col20']/child::div/child::a[@href='https://demo.smart-hospital.in/admin/pathology/gettestreportbatch']")
    pathologytest = (By.XPATH,"//a[@class='btn btn-primary btn-sm pathology']")
    testlist = (By.XPATH,"//h3[@class='box-title titlefix']")
    
    
    radiology = (By.XPATH,"//div[@class='col-lg-2 col-md-3 col-sm-6 col20']/child::div/child::a[@href='https://demo.smart-hospital.in/admin/radio/gettestreportbatch']")  
    radiologybill = (By.XPATH,"//h3[@class='box-title titlefix']")
    radiologytestlist = (By.XPATH,"//h3[@class='box-title titlefix']")
    
      
    bloodbank= (By.XPATH,"//div[@class='col-lg-2 col-md-3 col-sm-6 col20']/child::div/child::a[@href='https://demo.smart-hospital.in/admin/bloodbank/issue']")
    status = (By.XPATH,"//h3[@class='box-title titlefix']")
    donordet = (By.XPATH,"//h3[@class='box-title titlefix']")
    issuedet = (By.XPATH,"//div[@class='table-responsive']")
    component = (By.XPATH,"//h3[@class='box-title titlefix']")
    
    ambulance = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/vehicle/getcallambulance']//div[@class='info-box-content']")
    calllist=(By.XPATH,"//div[@class='content-wrapper']//div[4]")
    ambulancelist = (By.XPATH,"//div[@class='box-header with-border']")
    
    
    generalinc = (By.XPATH,"//a[@href='https://demo.smart-hospital.in/admin/income']//span[@class='info-box-icon bg-green']")
    incomelist = (By.XPATH,"//h3[@class='box-title titlefix']")
    
    expenses = (By.XPATH,"//div[@class='info-box']/child::a[@href='https://demo.smart-hospital.in/admin/expense']")
    expenselist = (By.XPATH,"//div[@class='box-header with-border']")
    
    