from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from PIL import ImageGrab


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Change these according to your screen
startY = 480
x1 = 710
x2 = 880
x3 = 1040
x4 = 1200

initialTime = time.time()
while keyboard.is_pressed('q') == False:
    runTime = time.time() - initialTime
    const = int(runTime*(0.5))
    if pyautogui.pixel(x1, startY)[0] == 0:
        click(x1, startY + const)
    if pyautogui.pixel(x2, startY)[0] == 0:
        click(x2, startY + const)
    if pyautogui.pixel(x3, startY)[0] == 0:
        click(x3, startY + const)
    if pyautogui.pixel(x4, startY)[0] == 0:
        click(x4, startY + const)

    