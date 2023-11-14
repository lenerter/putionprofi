import pyautogui
import keyboard
import time
a = int(input("Что будем гуглить "))
time.sleep(1)
pyautogui.hotkey('win', 'd')
if a == 1:
    time.sleep(1)
    pyautogui.moveTo(840, 525)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('hfpevty kb z?')
    time.sleep(1)
    pyautogui.press('enter')
elif a == 2:
    time.sleep(1)
    pyautogui.moveTo(840, 525)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('Ckfdf hj,jnfv!')
    time.sleep(1)
    pyautogui.press('enter')