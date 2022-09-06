# testing animation for game of life
# refrecned https://www.geeksforgeeks.org/python-create-simple-animation-for-console-based-application/

# importing the necessary packages
import time
import sys
import os
# import keyboard  # keyboard module needs to be installed using pip

def clear():
     # for windows OS
    if os.name =="nt":
        os.system("cls")
    else:# for linux / Mac OS
        os.system("clear")

# main
clear() #get rid of terminal prompt 
frame = 0

while frame < 100:
    print(frame)
    time.sleep(1) 
    clear()
    frame += 1

    if(keyboard.is_pressed()):
        exit()
