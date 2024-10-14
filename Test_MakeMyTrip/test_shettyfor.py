import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

driver.maximize_window()
time.sleep(10)
items = driver.find_elements(By.CSS_SELECTOR, ".card")
# print(items)
time.sleep(5)
for i in items:
    name = i.find_element(By.CSS_SELECTOR, ".card-title").text
    print(name)
    if name == "iphone X":
        i.find_element(By.TAG_NAME, "button").click()
        break
time.sleep(5)



# driver.find_element(By.XPATH,"//*[@class = 'react-autosuggest__input react-autosuggest__input--open']").send_keys("Bang")
# driver.find_element(By.XPATH,"//input[@title='From']")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='fromCity']").get_attribute()
