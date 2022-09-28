import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time
from utilities.readproperties import ReadConfig


class Test_001_Login:
    #baseURL = "https://admin-demo.nopcommerce.com/"
    baseURL=ReadConfig.getApplicationURL('self')

    #username= "admin@yourstore.com"
    username=ReadConfig.getUseremail('self')

    #password= "admin"
    password=ReadConfig.getPassword('self')


    def test_HomePageTitle(self,setup):
        #self.driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            assert False

    def test_Login(self,setup):
        #self.driver=webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()
        act_title=self.driver.title
       # self.driver.close()

