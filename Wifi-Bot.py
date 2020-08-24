import os
import sys

saved_networks = os.popen('netsh wlan show profiles').read()
#print(saved_networks)

available_networks = os.popen('netsh wlan show networks').read()
#print(available_networks)
