import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.Bussearchresult import BusSearhResult

price_list = []
bus_elements = []
second_cheapest_bus = None
class BusPage:
    # driver = webdriver.Chrome()
    # driver.find_elements(By.XPATH,"").

    def __init__(self, driver):
        self.driver = driver

    submitbutton = (By.CSS_SELECTOR,'button#search_button')
    searchbutton = (By.XPATH,"//*[@id='search_button']")
    # fromcity = (By.ID,"fromCity")
    fromcity = (By.XPATH,"//*[@id='fromCity']")

    gettomorrow = (By.XPATH,"//*[@data-testid='travelDate']")
    getfromlist = (By.CSS_SELECTOR,".sr_city")
    gettolist = (By.CSS_SELECTOR,".sr_city")
    # tocity = (By.ID, "toCity")
    tocity = (By.XPATH,"//input[@title='To']")
    # searchbtn = (By.CSS_SELECTOR, "#search_button")
    searchbtn = (By.ID, "search_button")
    sortCheapest = (By.XPATH,"//*[contains(text(), 'Cheapest')]")
    busprices = (By.CSS_SELECTOR, "#price")



    # sendcityname = (By.XPATH,"//input[@title='From']")
    sendcityname = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")

    def clikSubmit(self):
        return self.driver.find_element(*BusPage.searchbutton)

    def clikSubmittest2(self):
        searchresult = self.driver.find_element(*BusPage.searchbutton).click()
        Bussearchpage = BusSearhResult(self.driver)
        return Bussearchpage

    def sendfromcity(self):
        self.driver.find_element(*BusPage.fromcity).click()
        time.sleep(5)
        return self.driver.find_element(By.XPATH,"//*[@aria-controls='react-autowhatever-1']")
        # return asd.send_keys("aaa")
        # return self.driver.find_element(*BusPage.sendcityname)

    def getTomorrow(self):
        self.driver.find_element(*BusPage.gettomorrow).click()
        return self.driver.find_element(By.CSS_SELECTOR,"#tomorrow_date")

    def getOtherdate(self):
        self.driver.find_element(*BusPage.gettomorrow).click()
        return self.driver.find_element(By.CSS_SELECTOR,"#other_date")

    def getFromList(self):
        return self.driver.find_elements(*BusPage.getfromlist)

    def getTolist(self):
        return self.driver.find_elements(*BusPage.gettolist)

    def sendTocity(self):
        return self.driver.find_element(*BusPage.tocity)

    def selectDate(self,tripdate):
        dates = self.driver.find_elements(By.CSS_SELECTOR, ".DayPicker-Day")
        time.sleep(2)
        for date in dates:
            day= date.get_attribute("aria-label")
            # if day == "Tue Oct 15 2024":
            if day == tripdate:
                return date

    def clickSearch(self):
        return self.driver.find_element(*BusPage.searchbtn)

    def clickCheapest(self):
        return self.driver.find_element(*BusPage.sortCheapest)

    def getBusPrice(self):
        prices = self.driver.find_elements(*BusPage.busprices)
        for price in prices:
            print(price)
            amount = price.text
            price_value = float(amount.replace('$', '').replace(',', ''))  # Remove currency symbols and commas if needed
            price_list.append(price_value)
        return price_list

    def BUScard(self):
        All_details = self.driver.find_elements(By.CSS_SELECTOR,'.busCardContainer')
        for i in All_details:
            j = i.find_element(By.CSS_SELECTOR, "#price").text
            q = i.find_element(By.CSS_SELECTOR, "[id*='bus_']").get_attribute('id')
            # q = i.find_element(By.CSS_SELECTOR, '#id').text
            price_value = float(j.replace('$', '').replace(',', ''))  # Remove currency symbols and commas if needed
            # price_list.append(price_value)
            price_list.append((int(price_value), q))
        # # return price_list
        #
        print(price_list)
        second_high = price_list[1][1]
        print(second_high)

        return self.driver.find_element(By.ID, second_high).click()

    def select_nth_highestBus(self):
        # listofbusid = self.BUScard()
        listofbusid = price_list.sort(key=lambda x: x[0])
        # listofbusid.sort(key=lambda x: x[0])

        largest = second_largest = 0
        for i,j in listofbusid:
            if i > largest:
                second_largest = largest
                largest = i
                second_cheapest_bus = None

# print(second_largest)
            elif i > second_largest and i != largest:
                second_largest = i
                second_cheapest_bus = j

        print(price_list)
        second_high = price_list[1][1]
        print(second_high)

        return self.driver.find_element(By.ID, second_high).click()
        # print(second_high.find_element(By.ID,'id'))



    def return_the_2nd_highest_bus_card(self):
        All_details = self.driver.find_elements(By.CSS_SELECTOR,'.busCardContainer')
        for i in All_details:
            j = i.find_element(By.CSS_SELECTOR, "#price").text
            q = i.find_element(By.CSS_SELECTOR, "[id*='bus_']").get_attribute('id')
            # q = i.find_element(By.CSS_SELECTOR, '#id').text
            price_value = float(j.replace('$', '').replace(',', ''))  # Remove currency symbols and commas if needed
            # price_list.append(price_value)
            price_list.append((int(price_value), q))

        largest = second_largest = float('-inf')
        for i,j in price_list:
            if i > largest:
                second_largest = largest
                largest = i
                second_cheapest_bus = j
            elif i > second_largest and i != largest:
                second_largest = i
                second_cheapest_bus = j
        print(second_cheapest_bus)
        return self.driver.find_element(By.ID, second_cheapest_bus).click()

    def select_2_cheapet_bus(self):
        smallest = second_smallest = float('inf')

        for i,j in price_list:
            if i < smallest:
                second_smallest = smallest  # Update second smallest before smallest
                smallest = i  # Update smallest
                second_cheapest_bus = j

            elif i < second_smallest and i != smallest:
                second_smallest = i
                second_cheapest_bus = j
        return self.driver.find_element(By.ID, second_cheapest_bus).click()


    def sri_second_cheapest_bus(self):
        buses_raw_prices = self.driver.find_elements(By.CSS_SELECTOR, '#price')
        all_prices = []
        for raw_price in buses_raw_prices:
            #below 2 lines to remove special characters from price string and take only integers and appending to a list
            fare_temp = re.findall(r'\d+', raw_price.text)
            all_prices.append(int(''.join(map(str, fare_temp))))

        all_prices.sort()
        second_lowest_price = all_prices[1]

        # below code is to click on the select seats button of the bus whose prices is equal to second lowest price
        buses_list = self.driver.find_elements(By.CSS_SELECTOR, '.busCardContainer')

        for bus in buses_list:
            g_price = bus.find_element(By.ID, 'price').text
            g_temp = re.findall(r'\d+', g_price)
            bus_price = int(''.join(map(str, g_temp)))

            if bus_price == second_lowest_price:
                # we can directly do "bus.click() to select the seat or we can navigate to select seats button from bus selector
                # bus.click()
                # return bus.find_element(By.XPATH, 'div[2]/div')
                return bus.find_element(By.CSS_SELECTOR, ".sc-jKJlTe")
                # return bus.find_element(By.XPATH,"//div[contains(text(),'Select Seats')]")











