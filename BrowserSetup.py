from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
public class BrowserSetup()

driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver.exe")
baseURL = "https://platform.cloudways.com/login"


def set_up():
    driver.get(baseURL)