import time

from selenium.webdriver.common.by import By


class BusSearhResult:

    clickonfrom= (By.CSS_SELECTOR, "#from")
    from_to_citytab = (By.XPATH,"//*[@data-testid = 'city-input']")
    from_to_citylist = (By.CSS_SELECTOR,".sr_city")

    # tocitynames= (BY.)

    def __init__(self,driver):
        self.driver = driver

    def sendfromcity(self):
        self.driver.find_element(*BusSearhResult.clickonfrom).click()
        time.sleep(5)
        return self.driver.find_element(*BusSearhResult.from_to_citytab)

    def selectfromcityname(self,fromcityname):
        Fromcitylist = self.driver.find_elements(*BusSearhResult.from_to_citylist)
        for city in Fromcitylist:
            name = city.text
            if name == fromcityname:
                city.click()
            break

    def sendtocity(self):
        return self.driver.find_element(*BusSearhResult.from_to_citytab)

    def selecttocityname(self,tocity):
        Tocitylist = self.driver.find_elements(*BusSearhResult.from_to_citylist)
        for city in Tocitylist:
            name = city.text
            print(name)
            if name == tocity:
                return city

# """"""
#     def selectdate(self):
#         self.driver.find_element(By.CSS_SELECTOR,"#other_date").click()
#         time.sleep(4)
#         datelist = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label]")
#         # print(datelist)
#         for i in datelist:
#             date = i.text
#             print(date)
#             if date == 'Sat Nov 23 2024':
#                 date.click()
# """"""
    def selectdate(self):
        self.driver.find_element(By.CSS_SELECTOR,"#other_date").click()
        time.sleep(4)
        dates = self.driver.find_elements(By.CSS_SELECTOR, ".DayPicker-Day")
        time.sleep(2)
        for date in dates:
            day= date.get_attribute("aria-label")
            # if day == "Tue Oct 15 2024":
            if day == 'Sat Nov 23 2024':
                return date

    def clicksearchbt(self):
        return self.driver.find_element(By.XPATH,"//button[contains(text(),'Search')]")



