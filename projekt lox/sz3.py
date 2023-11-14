import pyautogui
import keyboard
import time
k=str(pyautogui.confirm(text="Завтра или послезавтра", title="Когда приём?", buttons=["завтра","послезавтра"]))
v=str(pyautogui.prompt(text="Завтра или послезавтра", title="Когда приём?", default="8:00"))
time.sleep(1)
pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey("winleft","r")
time.sleep(1)
pyautogui.write("notepad")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
keyboard.write('У вас '+k+' приём у стамотолога в '+v)
pyautogui.hotkey("ctrl","s")
    


