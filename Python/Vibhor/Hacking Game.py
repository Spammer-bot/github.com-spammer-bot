import time
import sys
import random
import os
print("Welcome to Hacking Terminal. ")
print("Selction of things you can hack !!")
print("1. Bal Bharati Public School Database")
print("2. Pakistan Air Defence System Database")
print("3. Nasa Database")
choise = int(input("Enter your choise from 1 to 3"))
if choise not in [1,2,3]:
    print("Invalid Choise")
    print("Enter the right Choise")
    sys.exit()
target_names = ["Bal Bharati Public School Database server", "Pakistan Cyber Cell server Database", "Nasa server Database " ]
target = target_names[int(choise)-1]
print("Connecting to "+target+"......")
time.sleep(10)
print("Establishing secure connection......")
spinner = ["|","/","-",'\\']
for i in range(50):
    sys.stdout.write('\b' + spinner[i%len(spinner)])
    sys.stdout.flush()
    time.sleep(0.1)
print("Bypassing firewall...")
for i in range(31):
    bar = '█' * i + '-' * (30 - i)
    percent = int((i / 30) * 100)
    sys.stdout.write(f'\r[{bar}] {percent}%')
    sys.stdout.flush()
    time.sleep(0.05)