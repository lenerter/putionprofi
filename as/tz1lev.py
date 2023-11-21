import pyautogui
import keyboard
import time
l=str("abeme")
p=str("1234q")
ul=str(input("Логин "))
up=str(input("Парль "))
if ul == "abeme":
    if up == "1234q":
        f=open('sus.txt', 'r', encoding="utf-8")
        str1 = f.readline()
        f.close()
        print(str1)
    else:
        pyautogui.alert(text="Пароль не верен", title="авторизация", button='Ок') 
else:
    pyautogui.alert(text="Логин не верен", title="авторизация", button='Ок') 