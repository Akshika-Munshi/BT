from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
def fileUpload():
         chromeOptions = webdriver.ChromeOptions()
         chromeOptions.binary_location = "/Users/avinashmunshi/Desktop/workspace3/BT/chromedriver"
         chromeDriver = "/chromedriver"
         driver = webdriver.Chrome(chromeDriver, options=chromeOptions)#(executable_path="/Users/avinashmunshi/Desktop/workspace3")#executable path may not be an attribute , may cause an error here
         driver.implicitly_wait(20)
         wait = WebDriverWait(driver, 10)
       
         driver.find_element(By.LINK_TEXT, 'upload a file')
         os.system("https://www.kidney.org/sites/default/files/styles/320_vert/public/Top%2031%20Car%20Memes%20You%20Will%20Want%20To%20Share%20-%20Kidney%20Cars.jpg?itok=jKIvBfWp")

fileUpload()