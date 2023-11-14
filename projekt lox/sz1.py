import pyautogui
import keyboard
import time
a = int(input("КАКУЮ ПАПКУ ОТКРЫТЬ "))
time.sleep(1)
pyautogui.hotkey('win', 'd')
if a == 1:
    time.sleep(1)
    pyautogui.moveTo(840, 525)
    time.sleep(1)
    pyautogui.doubleClick()

elif a == 2:
    time.sleep(1)
    pyautogui.moveTo(901, 541)
    time.sleep(1)
    pyautogui.doubleClick()

elif a == 3:
    time.sleep(1)
    pyautogui.moveTo(997, 541)
    time.sleep(1)
    pyautogui.doubleClick()
else:
    pass










