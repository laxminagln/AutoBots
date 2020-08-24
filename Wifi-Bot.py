import os                                                                       #importing os
import sys                                                                      #importing sys

saved_networks = os.popen('netsh wlan show profiles').read()                    #reading saved networks through pipe
#print(saved_networks)

available_networks = os.popen('netsh wlan show networks').read()                #reading available networks through pipe
#print(available_networks)

preferred_ssid = input('Enter the preferred network name:')                     #input the preferred network name

response = os.popen('netsh wlan disconnect').read()                             #disconnects currently connected network
#print(response)

if preferred_ssid not in saved_networks:                                        #checks if ssid id in saved list
  print("Profile for "+preferred_ssid+" is not saved in the system")
  print("Sorry, can't establish the connection"
  sys.exit()                                                                    #exits everything
else:
  print("Profile for "+preferred_ssid+" is present in the system")

"""
while True:
  avail = os.popen('netsh wlan show networks').read()
  #sleep(3)
  if preferred_ssid in avail:
    print("found")
    break
"""
print("---------connecting------------")
resp = os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()       #connects to the given ssid network
#print(resp)
print("connection request was completed successfully")
