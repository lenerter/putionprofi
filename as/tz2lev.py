import pyautogui
import keyboard
import time
row=str(pyautogui.confirm(text="Что зделать с фаилом", title="БЛАКНАТ.ОНЛАИН", buttons=["r","w"]))
if row == "r":
    f=open('sus.txt', 'r', encoding="utf-8")
    str1 = f.readline().strip()
    f.close()
    print(str1)
elif row == "w":
    f=open('sus.txt', 'w', encoding="utf-8")        
    f.write(input("новый текст "))
    f.close()
