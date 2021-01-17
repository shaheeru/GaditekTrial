from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

class Login():
    def __init__(self,drv):
        self.drv=drv
        #self.wait_variable = W(self.drv,self.wait_time_out)

    def LoginToApplication(self):
        self.drv.implicitly_wait(30)

        self.drv.find_element_by_id("userEmail").send_keys("shaheer.uddin94@gmail.com")
        self.drv.find_element_by_name("password").send_keys("Test123@@")
        # inputting values
        self.drv.find_element_by_xpath("//button[@type='submit']").click()


