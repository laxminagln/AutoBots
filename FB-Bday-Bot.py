from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

user_id = input("Enter your userid:")
password = input("Enter your password:")                                    #login details

browser = webdriver.Chrome("path to webdriver")
browser.get('https://www.facebook.com')                                     #reaches site

user_box = browser.find_element_by_id("email")
user_box.send_keys(user_id)                                                 #enters id

pass_box = browser.find_element_by_id("pass")
pass_box.send_keys(password)                                                #enters password

login_box = browser.find_element_by_id("u_0_b")
login_box.click()                                                           #login

time.sleep(20)

k = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'      #html part
n = browser.find_element_by_xpath(k).get_attribute('textContent')           #finds element by html part name
num = n[0]
num = int(num)                                                              #number of people
#print(num)

message = "Happy Birthday!"                                                 #message to be typed
browser.get("https://www.facebook.com/events/birthdays")                    #goes to birthday page
#time.sleep(3)

bday_list = browser.find_elements_by_xpath("//*[@class = 'enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
                                                                            #finds element by class
c = 0
for element in bday_list:                                                   #for loop
  element_id = str(element.get_attribute('id'))                             #id of html part
  XPATH = '//*[@id = "' +element_id+ '"]'                                   #html part
  post = browser.find_element_by_xpath(XPATH)                               #finds the html part
  post.send_keys(message)                                                   #enters the message
  #time.sleep(1)
  post.send_keys(Keys.RETURN)                                               #sends the message
  c = c+1                                               
  if(c>num):                                                                #checks if any more people
    break                                                                   #breaks the loop

browser.quit()                                                              #closes browser
