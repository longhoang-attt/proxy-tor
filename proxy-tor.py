#!/usr/bin/python
import time
import os
import subprocess


#####################-check-appps

try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')
try:

    check_proxychains = subprocess.check_output('which proxychains', shell=True)
except subprocess.CalledProcessError:

    print('[+] proxychains is not installed !')
    subprocess.check_output('sudo apt install proxychains -y',shell=True)
    print('[!] proxychains  is installed succesfully ')

def change():
os.system("sudo service tor start >> /dev/null && sudo service tor reload >> /dev/null && sudo proxychains curl icanhazip.com ")

##################################- start
os.system("clear")
print('''\033[1;32;40m \n


██████  ██████   ██████  ██   ██ ██    ██       ████████  ██████  ██████  
██   ██ ██   ██ ██    ██  ██ ██   ██  ██           ██    ██    ██ ██   ██ 
██████  ██████  ██    ██   ███     ████   █████    ██    ██    ██ ██████  
██      ██   ██ ██    ██  ██ ██     ██             ██    ██    ██ ██   ██ 
██      ██   ██  ██████  ██   ██    ██             ██     ██████  ██   ██ 
                                                                          
                                                                          
                               [ FROM : longhoang.attt ] v 1.0

''')
print("\033[1;40;31m contact : longhoang.attt@gmail.com \n
")
print("\033[1;32;40m Tools to keep you anonymous on your website and access the deepweb more easily than ever before \n")
time.sleep(1)
x = input("[+] time to change Ip in Sec >_  ")
lin = input("[+] how many time do you want to change your ip , for infinte ip change type >_ ")
if int(lin) ==int(0):
    while True:
        try:
            time.sleep(int(x))
            change()
        except KeyboardInterrupt:
            quit()
else:
    for i in range(int(lin)):
            time.sleep(int(x))
            change()

