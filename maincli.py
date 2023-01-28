import time
import random
import pyperclip # requires pyperclip by "pip install pyperclip"

while(True):
    password_length=int(input("Please input password length : "))
    if password_length<8:
        print("Your password length is too short")
    elif password_length>50:
        print("Your password length is too long")
    else:
        break
characters = "qwertyuiopasdfghjkl;'zxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM<>1234567890-_=+"

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated: {}".format(password))
time.sleep(1)
while(True):
    cp=input("Copy password? (y/n): ")
    if cp=='y':
        pyperclip.copy(password)
        break
    elif cp=='n':
        break
    else:
        print("Invalid answer")
        time.sleep(1)

