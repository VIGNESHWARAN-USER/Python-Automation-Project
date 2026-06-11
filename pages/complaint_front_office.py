from selenium.webdriver.common.by import By


class ComplaintFoPages:

    recbtnfo = (By.XPATH, "//a[normalize-space()='Receptionist']")
    signinfo = (By.XPATH, "//button[@type='submit']")
    frontofc = (By.XPATH, "//span[text()='Front Office']")
    complaint = (By.XPATH, "//a[contains(text(),'Complain')]")
    addcomp = (By.XPATH, "//a[contains(@class,'complain')]")
    comtype = (By.XPATH, "//select[@name='complaint']")
    src = (By.XPATH, "//select[@name='source']")
    complainby = (By.XPATH, "//input[@name='name']")
    phone = (By.XPATH, "//input[@name='contact']")
    date = (By.XPATH, "//input[@id='date']")
    desc = (By.XPATH, "//textarea[@name='description']")
    actiontaken = (By.XPATH, "//div[@class='ptt10']//input[@name='action_taken']")
    assigned = (By.XPATH, "//div[@class='ptt10']//input[@name='assigned']")
    note = (By.XPATH, "//div[@id='myModal']//div[9]//div[1]//textarea[1]")
    savebtn = (By.XPATH, "//button[@id='formaddbtn']//i[@class='fa fa-check-circle']")
    checklistcomp = (By.XPATH, "//h3[@class='box-title titlefix']")
    emptyfields = (By.XPATH, "//*[contains(text(),'required')]")
