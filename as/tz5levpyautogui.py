import pyautogui
import keyboard
import time

k=str(pyautogui.confirm(text="Что нарисовать", title="ПАИНТ.ОНЛАИН", buttons=["квадрат","круг","домик"]))
time.sleep(1)
pyautogui.moveTo(176, 1059)
pyautogui.click()
time.sleep(1)
pyautogui.write('Paint')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
if k == "квадрат":
    pyautogui.moveTo(19, 186)
    time.sleep(1)
    pyautogui.moveTo(627, 78)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(19, 186)
    time.sleep(1)
    pyautogui.dragTo(366, 515, button='left')
    pyautogui.moveTo(400, 600)
    pyautogui.click()
    time.sleep(1)
    print("Всё")
if k == "круг":
    pyautogui.moveTo(19, 186)
    time.sleep(1)
    pyautogui.moveTo(607, 76)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(19, 186)
    time.sleep(1)
    pyautogui.dragTo(366, 515, button='left')
    pyautogui.moveTo(400, 600)
    pyautogui.click()
    time.sleep(1)
    print("Всё") 
if k == "домик":
    pyautogui.moveTo(19, 250)
    time.sleep(1)
    pyautogui.moveTo(627, 78)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(19, 250)
    time.sleep(1)
    pyautogui.dragTo(366, 515, button='left')
    pyautogui.moveTo(400, 600)
    pyautogui.click()
    time.sleep(1)
    
    pyautogui.moveTo(700, 76)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(19, 250)
    time.sleep(1)
    pyautogui.dragTo(368, 181, button='left')
    time.sleep(1)
    pyautogui.moveTo(400, 600)
    pyautogui.click()
    time.sleep(1)
    print("Всё")

