import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:

    # logintab = ((By.XPATH,"//*[@class='modalMain tcnFooter']"))


    def close_cred_popup(self):
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='modalMain tcnFooter']")))
        # return self.driver.find_element(By.XPATH,"//*[@class='commonModal__close']")
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='modalMain tcnFooter']")))
            # self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH,"//*[@class='commonModal__close']").click()
        except:
            print("Login popup is not displayed")


    def confirm_search_resutl(self):
        wait = WebDriverWait(self.driver, 15)

        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[class*='modalMain']")))
        wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'End of')]")))

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # filehandler = logging.FileHandler('Report\logfile.log')
        filehandler = logging.FileHandler('C:\\Users\\swashint\\PycharmProjects\\MakeMyTrip\\Utilities\\logfile.log')
        # filehandler = logging.FileHandler('C:\Users\swashint\PycharmProjects\MakeMyTrip\Utilities\logfile.log')
        # filehandler = logging.FileHandler('C://Users//swashint//PycharmProjects//MakeMyTrip//Utilities//logfile.log')
        # filehandler = logging.FileHandler('C:/Users/swashint/PycharmProjects/MakeMyTrip/Utilities/logfile.log')

        # filehandler = logging.FileHandler('Utilities\\logfile.log')

        # formatter = logging.Formatter(" %(levelname)s : %(name)s : %(message)s")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger


