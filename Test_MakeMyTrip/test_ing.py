import textwrap
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

price_list =[]
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com")
time.sleep(5)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[class*='modalMain']")))
# wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='modalMain tcnFooter']")))

time.sleep(4)

## testing the login pop-up

# driver.switch_to.frame((By.ID,'gsi_214100_639326'))
# driver.switch_to.frame('gsi_214100_639326')
# iframe = driver.find_elements(By.CSS_SELECTOR,".g_id_signin")
# driver.switch_to.frame((By.CSS_SELECTOR,".S9gUrf-YoZ4jf']"))
# driver.switch_to.frame((By.XPATH, "//iframe[@id='gsi_681102_490497']"))

# driver.find_element(By.CSS_SELECTOR,".nsm7Bb-HzV7m-LgbsSe Bz112c-LgbsSe hJDwNd-SxQuSe i5vt6e-Ia7Qfc JGcpL-RbRzK").click()


# (//iframe[@id='gsi_681102_490497'])[1]
# //iframe[@id='gsi_681102_490497']
main_w = driver.current_window_handle
print(main_w)

driver.find_element(By.CSS_SELECTOR,".S9gUrf-YoZ4jf").click()
# driver.switch_to.frame(iframe)
time.sleep(5)
win = driver.window_handles
print(win)
driver.switch_to.window(win[1])
# driver.find_element(By.XPATH,"//*[contains(text(), 'Create account')]").click()

email = driver.find_element(By.XPATH,"//*[@type='email']")
email.click()
time.sleep(2)
email.send_keys("bbb282110@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(text(),'Next')]").click()
time.sleep(1)
driver.get_screenshot_as_file("qqq.png")
driver.find_element(By.CSS_SELECTOR,".Xb9hP").send_keys("Asdfg@12345")
time.sleep(2)
driver.find_element(By.XPATH,"//*[contains(text(),'Next')]").click()
time.sleep(5)
# driver.get_screenshot_as_png()
# driver.find_element(By.XPATH,"//*[@id='fromCity']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@title='From']").send_keys("Bang")
# fromcities = driver.find_elements(By.CSS_SELECTOR,".sr_city")
# for city in fromcities:
#     cityattr = city.text
#     if cityattr == "Bangalore, Karnataka":
#         city.click()
#         break
# driver.find_element(By.ID, "search_button").click()
# time.sleep(5)
# driver.get_screenshot_as_file('sn.png')
# driver.find_element(By.ID, "search_button").get_attribute(id)
# driver.find_element(By.XPATH,"//*[@id='toCity']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@title='To']").send_keys("Nip")
# time.sleep(2)
# tocities = driver.find_elements(By.CSS_SELECTOR,".sr_city")

#test for geting the fares -
# prices = driver.find_elements(By.CSS_SELECTOR, "#price")
# for price in prices:
#     # amount = price.get_attribute(textwrap).text
#     amount = price.text
#     print(amount)

# All_details = driver.find_elements(By.CSS_SELECTOR,'.busCardContainer')
# for i in All_details:
#     j = i.find_element(By.CSS_SELECTOR, "#price").text
#     q = i.find_element(By.CSS_SELECTOR,'')
#     price_value = float(j.replace('$', '').replace(',', ''))  # Remove currency symbols and commas if needed
#     # price_list.append(price_value)
#     price_list.append((int(price_value)))
# print(price_list)



#
#
# for Tcity in tocities:
#     cityname = Tcity.text
#     print(cityname)
#     if cityname == "Nippani, Karnataka":
#         Tcity.click()
#         break
# time.sleep(2)
# dates =driver.find_elements(By.CSS_SELECTOR, ".DayPicker-Day")
# time.sleep(2)
#
# for date in dates:
#     day= date.get_attribute("aria-label")
#     print(day)
#     if day == "Tue Oct 15 2024":
#         date.click()
#         break
# time.sleep(20)
#


# driver.find_element(By.XPATH,"//*[@class = 'react-autosuggest__input react-autosuggest__input--open']").send_keys("Bang")
# driver.find_element(By.XPATH,"//input[@title='From']")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='fromCity']").get_attribute()

# All_details = driver.find_elements(By.CSS_SELECTOR,'.busCardContainer')
# for i in All_details:
#     j = i.find_element(By.CSS_SELECTOR, "#price").text
#     q = i.find_element(By.CSS_SELECTOR, "[id*='bus_']").get_attribute('id')
#     # q = i.find_element(By.CSS_SELECTOR, '#id').text
#     price_value = float(j.replace('$', '').replace(',', ''))  # Remove currency symbols and commas if needed
#     # price_list.append(price_value)
#     price_list.append((int(price_value), q))
#
# largest = second_largest = 0
# for i,j in price_list:
#     if i > largest:
#         second_largest = largest
#         largest = i
#         second_cheapest_bus = j
#     elif i > second_largest and i != largest:
#         second_largest = i
#         second_cheapest_bus = j
#     print(second_cheapest_bus)


