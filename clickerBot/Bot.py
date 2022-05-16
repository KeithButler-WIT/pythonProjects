#!/usr/bin/env python3

from pyautogui import *
import pyautogui
import time
import keyboard
import random

# def click():
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed(81) == False:
    if pyautogui.pixel(2335,360)[0]  == 0:
        pyautogui.click(2335,360)
        # click(2335,360)
    if pyautogui.pixel(2411,360)[0]  == 0:
        pyautogui.click(2411,360)
        # click(2411,360)
    if pyautogui.pixel(2450,360)[0]  == 0:
        pyautogui.click(2450,360)
        # click(2450,360)
    if pyautogui.pixel(2558,360)[0]  == 0:
        pyautogui.click(2558,360)
        # click(2558,360)
