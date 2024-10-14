import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from PageObject.Homepage import HomePage
from Utilities.Baseclass import BaseClass


class Test_MakeMyTrip(BaseClass):
    # driver = webdriver.Chrome()
    
    @pytest.mark.first
    def test_BanToPune(self):
        log = self.getlogger()
        self.close_cred_popup()
        # self.driver.find_element(By.XPATH,"//*[@class='commonModal__close']").click()
        Homepage = HomePage(self.driver)
        Busespage = Homepage.selectBus()
        Busespage.sendfromcity().send_keys("Bang")
        fromcities = Busespage.getFromList()
        for city in fromcities:
            cityattr = city.text
            if cityattr == "Bangalore, Karnataka":
                city.click()
                break
        Busespage.sendTocity().send_keys("Nipp")
        time.sleep(3)
        tocities = Busespage.getTolist()
        for city in tocities:
            cityname = city.text
            if cityname == "Nippani, Karnataka":
                city.click()
                break
        dates =self.driver.find_elements(By.CSS_SELECTOR, ".DayPicker-Day")
        # Busespage.selectDate("Tue Oct 15 2024")
        # asd.click()
        Busespage.selectDate("Tue Oct 15 2024").click()
        Busespage.clickSearch().click()
        self.confirm_search_resutl()
        log.info("msg displayed")
        Busespage.clickCheapest().click()
        asd = Busespage.sri_second_cheapest_bus().click()
        log.info(asd)
        self.driver.get_screenshot_as_file('Screenshot/first.png')
        self.driver.find_element(By.CSS_SELECTOR,".chMmtLogo").click()
        # asd.find_element(By.XPATH, "//*[@data-test-id='select-seats']").click()
        # time.sleep(14)


    @pytest.mark.second
    def test_modify_from_date_search_page(self):
        log = self.getlogger()
        self.close_cred_popup()
        # time.sleep(45)
        # popup = self.close_cred_popup()
        # popup.click()
        Homepage = HomePage(self.driver)
        Busespage = Homepage.selectBustest2()
        self.driver.get_screenshot_as_file("2nd.png")
        BussSearchPage = Busespage.clikSubmittest2()
        BussSearchPage.sendfromcity().send_keys("Bang")
        BussSearchPage.selectfromcityname('Bangalore, Karnataka')
        BussSearchPage.sendtocity().send_keys("Nipp")
        BussSearchPage.selecttocityname('Nippani, Karnataka').click()
        BussSearchPage.selectdate().click()
        BussSearchPage.clicksearchbt().click() #fails

        # self.driver.get_screenshot_as_file('Screenshot/second.png')
        self.driver.find_element(By.CSS_SELECTOR,".chMmtLogo").click()


    @pytest.mark.third
    def test_fill_loginpopup(self):
        log = self.getlogger()
        self.close_cred_popup()
        # time.sleep(45)
        # popup = self.close_cred_popup()
        # popup.click()
        Homepage = HomePage(self.driver)
        # self.driver.get("https://www.makemytrip.com/")
        Homepage.click_loginorcreateaccount().click()
        Homepage.sendPhoneNo().send_keys("8147749854")
        # self.driver.get_screenshot_as_file("third.png")
        log.info("hello")
        self.driver.find_element(By.XPATH,"//*[@class='commonModal__close']").click()
        time.sleep(2)
        # Homepage.clickContinue().click()
        # msg = Homepage.getMsg()
        # if msg == 'Verify Your Mobile Number':
        #     log.info("correct")
        # else:
        #     log.info('wrong')
        # popup.click()
        # time.sleep(3)
        self.driver.get_screenshot_as_file("Screenshot/third.png")
        # self.driver.find_element(By.CSS_SELECTOR,".chMmtLogo").click()

    @pytest.mark.fourth
    def test_scroll_down(self):
        action = ActionChains(self.driver)
        self.close_cred_popup()
        # Homepage = HomePage(self.driver)
        # popup = self.close_cred_popup()
        # popup.click()
        # img = self.driver.find_element(By.XPATH,"//img[@alt='Make My Trip']")
        # action.context_click(img).perform()
        time.sleep(5)
        qr = self.driver.find_element(By.CSS_SELECTOR,".icQRCode")
        action.scroll_to_element(qr).perform()
        time.sleep(3)
        self.driver.get_screenshot_as_file("Screenshot/fourth.png")
        # action.double_click(driver.find_element(By.XPATH,"sf")).perform()
        # find_element(By.XPATH,"//*[contains(text(),'Shop')]")
        self.driver.find_element(By.CSS_SELECTOR,".chMmtLogo").click()

    @pytest.mark.fifth
    def test_copyBusOfferCode(self):
        self.close_cred_popup()
        # asd = self.driver.title
        # print("the output is " + asd)
        Hopeepage = HomePage(self.driver)
        Hopeepage.budOffer().click()
        self.driver.find_elements(By.CSS_SELECTOR, ".cardInnerInfo")[0].click()
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(3)
        self.driver.find_element(By.ID,"buses_0").click()
        gh = self.driver.find_elements(By.CSS_SELECTOR,".saleCouponCode")[0]
        # for i in gh:
        #     print(i.text)
        print(gh.text)
        #
        action=ActionChains(self.driver)
        action.double_click(gh).perform()
        # action.context_click(gh).perform()
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        self.driver.find_element(By.XPATH,"//img[@alt='MakeMyTrip']").click()
        fr = self.driver.find_element(By.CSS_SELECTOR,"#fromCity")
        fr.click()
        time.sleep(3)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.close()
        self.driver.switch_to.window(handles[0])

        self.driver.get_screenshot_as_file("fifth.png")

        # self.driver.find_element(By.XPATH,"//*[@alt='MakeMyTrip']").click()


















