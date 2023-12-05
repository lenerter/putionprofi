import pyautogui
import keyboard
import time
searc = str(input("Что будем гуглить? "))

time.sleep(1)
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.moveTo(525, 1066)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.moveTo(218, 61)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.write(searc)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click()

time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('win', 'd')
time.sleep(1)

pyautogui.moveTo(1852, 889)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.moveTo(249, 330)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(290, 310)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(searc)
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.moveTo(525, 1066)
time.sleep(1)
pyautogui.doubleClick()







