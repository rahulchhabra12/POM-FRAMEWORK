from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[1]/div[1]/input').send_keys("Rahul")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[1]/div[2]/input').send_keys("Chhabra")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[2]/div/textarea').send_keys("Barara AMBALA")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[3]/div[1]/input').send_keys("rahulchhabra956@gmail.com")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[4]/div/input').send_keys("8816805168")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[5]/div/label[1]/input').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[6]/div/div[1]/input').click()
time.sleep(5)
#driver.find_element(By.ID, 'checkbox3').click()
#driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[7]/div/multi-select/div[2]/ul/li[8]/a').click()
#driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a').click()

#driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')


var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[9]/div/select'))
var.select_by_visible_text("Select Country")


var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[8]/div/select'))
var.select_by_visible_text("CSS")



var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[10]/div/select'))
var.select_by_visible_text("India")

var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[11]/div[1]/select'))
var.select_by_visible_text("2000")

var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[11]/div[2]/select'))
var.select_by_visible_text("May")

var=Select(driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[11]/div[3]/select'))
var.select_by_visible_text("1")

driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[12]/div/input').send_keys("Rahul@123")
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[13]/div/input').send_keys("Rahul@123")
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/form/div[14]/div/button[1]').click()




#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a'))).click()



