from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

user_id = input("Enter your userid:")
password = input("Enter your password:")

browser = webdriver.Chrome("path to webdriver")
browser.get('https://www.facebook.com')

user_box = browser.find_element_by_id("email")
user_box.send_keys(user_id)

pass_box = browser.find_element_by_id("pass")
pass_box.send_keys(password)

login_box = browser.find_element_by_id("u_0_b")
login_box.click()

time.sleep(20)

k = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n = browser.find_element_by_xpath(k).get_attribute('textContent')
num = n[0]
num = int(num)
#print(num)

message = "Happy Birthday!"
browser.get?("https://www.facebook.com/events/birthdays")
#time.sleep(3)

bday_list = browser.find_elements_by_xpath("//*[@class = 'enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
