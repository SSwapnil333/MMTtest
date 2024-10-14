from selenium.webdriver.common.by import By

from PageObject.Busespage import BusPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Busbutton = (By.CSS_SELECTOR,'.menu_Buses')
    Trainbutton = (By.CSS_SELECTOR,'.menu_Trains')
    loginbtn = (By.CSS_SELECTOR,".userLoggedOut")
    SendPhno = (By.CSS_SELECTOR,".fullWidth")
    # clickContinuebtn = (By.XPATH,"//span[contains(text(),'Continue')]")
    # clickContinuebtn = (By.XPATH,"//button[@class='capText font16']")
    clickContinuebtn = (By.XPATH,"//button[@data-cy='continueBtn']")
    verifymsg = (By.CSS_SELECTOR,".modalTitle")
    busoffer = (By.CSS_SELECTOR, "[id*= 'Tab_BUS']")



    def selectBus(self):
        self.driver.find_element(*HomePage.Busbutton).click()
        BusesPage = BusPage(self.driver)
        return BusesPage


    def selectTrain(self):
        return self.driver.find_element(*HomePage.Trainbutton)

    def selectBustest2(self):
        self.driver.find_element(*HomePage.Busbutton).click()
        BusesPage = BusPage(self.driver)
        return BusesPage

    def click_loginorcreateaccount(self):
        return self.driver.find_element(*HomePage.loginbtn)

    def sendPhoneNo(self):
        self.driver.find_element(*HomePage.SendPhno).click()
        return self.driver.find_element(*HomePage.SendPhno)

    def clickContinue(self):
        return self.driver.find_element(*HomePage.clickContinuebtn)

    def getMsg(self):
        return self.driver.find_element(*HomePage.verifymsg).text

    def budOffer(self):
        return self.driver.find_element(*HomePage.busoffer)


