from selenium import webdriver                            #importing libraries

browser = webdriver.Chrome('path to driver')              #give path to your chrome driver

phone_num = input("enter your phone number:")             #enter your phone number
times = int(input("enter number of times:"))              #number of times

browser.get("https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
                                                          #goes to the login page of amazon.in
phone = browser.find_element_by_id("ap_email")            #gets the text box for email or phone number
phone.send_keys(phone_num)                                #enters phone number automatically

cnt = browser.find_element_by_id("continue")              #gets the button for continuing the process of login
cnt.click()                                               #clicks the button

sendOTP = browser.find_element_by_id("continue")          #finds the get otp button
sendOTP.click()                                           #clicks on that button

n = times-1                                               #since 0 to n = times
for i in range(n):                                        #for loop
  r = browser.find_element_by_link_text("Resend OTP")     #finds the resend otp link
  r.click                                                 #clicks the link
browser.quit()                                            #quits the browser
