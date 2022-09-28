from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"

    #button_login_xpath="//input[@class='button-1login-button']"
    link_logout_linktext="logout"

    def __init__(self,driver):
        self.driver=driver
        #driver=webdriver.Chrome(executable_path="C:\Users\hp\Downloads\chromedriver_win32")

    def setUserName(self,username):
       # self.driver.find_element_by_id(self.textbox_username_id).clear()
        #self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
       self.driver.find_element("id", "Email").clear()
       time.sleep(5)
       self.driver.find_element("id","Email").send_keys(username)

    def setPassword(self,password):
      #  self.driver.find_element_by_id(self.textbox_password_id).clear()
        #self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
          self.driver.find_element("id", "Password").clear()
          self.driver.find_element("id", "Password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath",'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
        time.sleep(4)

        #self.driver.find_element_by_xpath(self.button_login_xpath).click()
         #self.driver.find_element(By.CLASS_NAME, 'button-1 login-button')


    def clickLogout(self):
        self.driver.find_element(By.XPATH, '/html/body/div[3]/nav/div/ul/li[3]/a').click()


