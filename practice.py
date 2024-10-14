# list1 = [1,4,6,7,6,7,3,4,64,643,3,6,2,6,4,7,642,24,5]
# list2=['1','4','8','3']
#
# list3 = list(zip(list2,list1))  # This will give indices with values from list1
# print(list3)
# # list.strip()
# #
# # # list.sort(reverse=True)
# #
# # print(list)
# largest = second_largest = 0
# for i in list1:
#     if i > largest:
#         second_largest = largest
#         largest = i
# # print(second_largest)
#     elif i > second_largest and i != largest:
#         second_largest = i
#
# print(second_largest)
#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Chrome()

# Open a page (for example purposes)
driver.get("https://www.makemytrip.com")
driver.maximize_window()
time.sleep(4)

# Get the handle for the current window (the main window)
main_window_handle = driver.current_window_handle
print("Main Window Handle:", main_window_handle)

# Assuming you've clicked on something that opened a new window
# e.g., driver.find_element(By.ID, "loginButton").click()
driver.find_element(By.CSS_SELECTOR,".S9gUrf-YoZ4jf").click()



# Get all the window handles (this includes the main window and the newly opened windows)
all_window_handles = driver.window_handles

print(all_window_handles)

# Print details of all the window handles
for idx, handle in enumerate(all_window_handles):
    print(f"Window {idx+1} Handle: {handle}")

# Example: Switch to each window and print its title
# for handle in all_window_handles:
#     driver.switch_to.window(handle)
#     print(f"Window Handle: {handle}, Window Title: {driver.title}")
#
# # Switch back to the main window (optional)
# driver.switch_to.window(main_window_handle)
#
# # Close the driver (optional)
# driver.quit()
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.get_screenshot_as_png()
