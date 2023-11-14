import pyautogui
import keyboard
import time
k=int(pyautogui.confirm(text="Кокой фаил отроть", title="КОПИРАКА.ОНЛАИН", buttons=["1","2","3"]))
time.sleep(1)
pyautogui.hotkey('win', 'd')

if k == 1:
    time.sleep(1)
    pyautogui.moveTo(843, 559)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.moveTo(885, 649)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    
if k == 2:
    time.sleep(1)
    pyautogui.moveTo(893, 550)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.moveTo(885, 649)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    
if k == 3:
    time.sleep(1)
    pyautogui.moveTo(967, 544)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.moveTo(885, 649)
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')    
    
    








