from selenium.webdriver.common.by import By

class AddVisitor:
    #search
    login = By.xpath("//a[text()='Login']");
    userlog = By.xpath("//p[@style='margin-top: 20px;']//a[@href='https://demo.smart-hospital.in/site/userlogin']");
    signup = By.xpath("//button[@type='submit'] | //button[contains(text(),'Sign')]");
    pathlogyMenu = By.xpath("//a[normalize-space()='Pathology']");
    search = By.xpath("//input[@type='search' or @placeholder='Search...']");
    filter = By.xpath("//div[text()='Records: 1 to 1 of 1 (filtered from 14 total records)']");
    table = By.xpath("//table//tr");
    notFound = By.xpath("//tr[@class='odd']//td[text()='No matching records found']");

    #pay
    paybtn = By.xpath("//td[contains(@class,'text-right')]//button[contains(@onclick,'payModal')]");
    payAmt = By.xpath("//input[@id='amount_total_paid']");
    add = By.xpath("//div[@class='modal-footer']//button[@id='pay_button']");
    makepay = By.xpath("//button[normalize-space()='Make Payment']");
    mobile = By.xpath("//input[@type='tel']");
    cont = By.xpath("//div[@class='bg-surface p-4 d:mt-2 d:px-0 px-0']//button[@type='button']");
    upi = By.xpath("//*[self::a or self::li or self::div or self::span][normalize-space()='UPI']");
    email = By.xpath("//input[contains(@placeholder,'upi') or contains(@placeholder,'UPI') or contains(@placeholder,'okhdfcbank') or contains(@placeholder,'@')]");
    verify = By.xpath("//button[contains(normalize-space(),'Verify') or contains(normalize-space(),'Pay') or contains(normalize-space(),'verify')]");
    succ = By.xpath("//div[@class='alert alert-success alert-dismissible']");
    payError = By.xpath("//*[contains(text(),'Amount Should Not Be Greater Than Balance')] | " + "//*[contains(text(),'Invalid Amount')]");
    frame = By.tagName("iframe");
	