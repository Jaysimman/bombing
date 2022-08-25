from email import message
import pyautogui as AJ
import time

message=input("Enter a message:")

time.sleep(10)

while True:

    AJ.typewrite(message)
    AJ.press("enter")