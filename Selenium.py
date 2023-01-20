from selenium import webdriver
browser = webdriver.Chrome()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = "/Users/avinashmunshi/Desktop/New Folder With Items/Google Chrome.app"
driver = webdriver.Chrome(chromeDriver, options=chromeOptions)
#(executable_path="C:\chromedriver.exe")

#driver.maximize_window()

browser.get("https://www.google.com/imghp?hl=en&tab=wi")
# #to identify element
# s = driver.find_element({id: 'e4JwSe'})
# #file path specified with send_keys
# s.send_keys("https://www.kidney.org/sites/default/files/styles/320_vert/public/Top%2031%20Car%20Memes%20You%20Will%20Want%20To%20Share%20-%20Kidney%20Cars.jpg?itok=jKIvBfWp")


#driver.findElement({id:'e4JwSe'}).sendKeys("https://www.kidney.org/sites/default/files/styles/320_vert/public/Top%2031%20Car%20Memes%20You%20Will%20Want%20To%20Share%20-%20Kidney%20Cars.jpg?itok=jKIvBfWp")

# browser.find_element_by_id(e4JwSe)
linkElem = browser.find_element_by_link_text("Paste image link")
linkElem.click()