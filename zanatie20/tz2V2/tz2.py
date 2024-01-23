import os
import pyautogui
import keyboard
import time

f = open('1.txt', 'r', encoding="utf-8")
txt = f.readline()
if txt == "тревога":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
elif txt == "подозрительно":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номера аварийных служб")
    pyautogui.hotkey('Enter')
    pyautogui.hotkey('ctrl', 't')
    keyboard.write("номер сантехника")
    pyautogui.hotkey('Enter')
else:
    pass

f.close()

f = open('2.txt', 'r', encoding="utf-8")
txt = f.readline()
if txt == "тревога":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
elif txt == "подозрительно":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номера аварийных служб")
    pyautogui.hotkey('Enter')
    pyautogui.hotkey('ctrl', 't')
    keyboard.write("номер сантехника")
    pyautogui.hotkey('Enter')
else:
    pass

f.close()

f = open('3.txt', 'r', encoding="utf-8")
txt = f.readline()
if txt == "тревога":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
elif txt == "подозрительно":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номера аварийных служб")
    pyautogui.hotkey('Enter')
    pyautogui.hotkey('ctrl', 't')
    keyboard.write("номер сантехника")
    pyautogui.hotkey('Enter')
else:
    pass

f.close()

f = open('4.txt', 'r', encoding="utf-8")
txt = f.readline()
if txt == "тревога":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
elif txt == "подозрительно":
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номера аварийных служб")
    pyautogui.hotkey('Enter')
    pyautogui.hotkey('ctrl', 't')
    keyboard.write("номер сантехника")
    pyautogui.hotkey('Enter')
else:
    pass

f.close()