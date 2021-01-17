from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time

class Team():
    def __init__(self,drv):
        self.drv=drv

    def AddMemberDetails(self):

        self.drv.maximize_window()
        self.drv.implicitly_wait(30)

        self.drv.find_element_by_xpath("//button[@title='View your Team members']").click()
        # click on team(link) on top  bar

        self.drv.find_element_by_xpath("//button[@ui-sref='team_create']").click()
        # click on add member button

        #x = datetime.datetime.now()
        x = time.time()
        y = str(x)
        print(y)
        self.drv.find_element_by_name('email').send_keys("test" + y + "@test.com")
        # adding email in the email field

        self.drv.find_element_by_name('name').send_keys("CloudwaysTestUser" + y)

        self.drv.find_element_by_xpath("//md-select[@name='jobTitle']").click()
        self.drv.find_element_by_xpath("//md-option[@value='Architect']").click()
        #select job title from dropdown

    def AddMemberWithBillingAccess(self):
        self.drv.find_element_by_xpath("//md-checkbox[@aria-label='Billing Access']").click()
        #select Billing access role

    def AddMemberWithLimitedConsoleAccess(self):
        self.drv.find_element_by_xpath("//md-checkbox[@aria-label='Console Access']").click()
        self.drv.find_element_by_xpath("//md-radio-button[@aria-label='limited access']").click()
        self.drv.find_element_by_xpath("//md-checkbox[@aria-label='Add Server']").click()



    def ClickAddMember(self):
        self.drv.find_element_by_xpath("//button[@aria-label='Add member']").click()