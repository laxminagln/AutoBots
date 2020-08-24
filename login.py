from selenium import webdriver                                  #imports webdriver module from selenium

browser = webdriver.Chrome("path to chromedriver")              #if Firefox, then path to firefox webdriver

browser.get("address of website")                               #type the address of the website you want to login

element_email = browser.find_element_by_id("id for username")   #find the id for username by inspecting and put it here
element_email.send_keys("your username")                        #type your username here

element_pw = browser.find_element_by_id("id for password")      #find the id for password by inspecting and put it here
element_pw.send_keys("your password")                           #type your password here

login = browser.find_element_by_id("id for login button")       #find the id for login by inspecting and put it here
login.click()                                                   #clicks the login button

#browser.quit()                                                 #quits the browser
