from selenium import webdriver
from selenium.webdriver.common.by import By


import time

driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://admin-demo.nopcommerce.com/")
time.sleep(10)

#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element("id", "Email").clear()

driver.find_element("id","Email").send_keys("admin@yourstore.com")

#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
driver.find_element("id", "Password").clear()
driver.find_element("id", "Password").send_keys("admin")

#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

driver.find_element("xpath",'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
time.sleep(4)
