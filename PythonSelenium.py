import time
from selenium import webdriver
from selenium.webdriver.common.by import By


import time


driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")

# driver.get("https://www.facebook.com/")
# print(driver.title)
# time.sleep(2)
# driver.get("https://www.google.com/")
# print(driver.title)
# time.sleep(2)
# driver.maximize_window()
# driver.minimize_window()
# driver.quit()

#driver.get("https://opensource-demo.orangehrmlive.com/")
#time.sleep(15)
#name=driver.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active').send_keys('Admin')
#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")

#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
#time.sleep(7)
#driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

#driver.find_element(By.XPATH,'/html/body').click()
# username.send_keys("Admin")
# password=driver.find_element("name",'password')
# username.send_keys("admin123")


#driver.get("https://testautomationpractice.blogspot.com/")

#driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()
#time.sleep(3)
#driver.switch_to.alert.accept()
#driver.switch_to.alert.accept()
#alert.accept()
driver.get("https://the-internet.herokuapp.com")

time.sleep(3)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(5)
#to refresh the browser
#driver.refresh()
#driver.find_element(By.LINK_TEXT,"Frames").click()
#driver.find_element(By.LINK_TEXT,"Nested Frames").click()
# to switch to frame with frame name
#driver.switch_to.frame("frame-bottom")
# to get the text inside the frame and print on console
#print(driver.find_element(By.XPATH,"//*[text()='BOTTOM']").text)
#print(driver.find_element(By.XPATH, '/html/body').text)
# to move out the current frame to the page level
#driver.switch_to.default_content()
#to close the browser
driver.quit()