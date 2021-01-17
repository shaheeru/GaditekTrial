from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from PageObject.Login import Login
from PageObject.Team import Team



driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
baseURL = "https://platform.cloudways.com/login"


def set_up():
    driver.get(baseURL)

def test_login_page():
    UserLogin = Login(driver)
    UserLogin.LoginToApplication()

def test_AddMemberDetails():
    memberDetails = Team(driver)
    memberDetails.AddMemberDetails()


def test_AddMemberWithBillingAccess():
    billingAccess = Team(driver)
    billingAccess.AddMemberWithBillingAccess()

def test_AddMemberWithLimitedConsoleAccess():
    limitedConsoleAccess = Team(driver)
    limitedConsoleAccess.AddMemberWithLimitedConsoleAccess()

#def test_ClickAddMember():
    addMember = Team(driver)
    addMember.ClickAddMember()

set_up()
test_login_page()
test_AddMemberDetails()
test_AddMemberWithBillingAccess()
test_AddMemberWithLimitedConsoleAccess()
test_ClickAddMember()
