from win32api import GetKeyState 
from win32con import VK_NUMLOCK
import random
import math
import pyautogui
import time

def PressKey(key):
    pyautogui.keyDown(key)

def ReleaseKey(key):
    pyautogui.keyUp(key)

def PressAndReleaseKey(key):
    pyautogui.press(key)

def Sleep(msec):
    time.sleep(msec / 1000)

while True:
    toggleLR= 0
    center = 0
    right = 0
    left = 0
    limit = 600
    over = False
    while GetKeyState(VK_NUMLOCK):
        wait = random.randint(100,800)
        PressAndReleaseKey("9")
        PressAndReleaseKey("q")
        if(center> limit or center < (0-limit) ):
            wait = math.abs(center)
            over = True
            center = 0
        else :
            over = False
        
        if(toggleLR== 0) :
            PressKey("a")
        else:
            PressKey("d")
        
        Sleep(wait)
        PressAndReleaseKey("9")

        if(toggleLR== 0) :
            ReleaseKey("a")
            PressAndReleaseKey("9")
            if(not over) : 
                center = center - wait
            toggleLR= 1
        else :
            ReleaseKey("d")
            PressAndReleaseKey("9")
            if(not over) : 
                center = center + wait
            toggleLR= 0

