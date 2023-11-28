import pyautogui
import keyboard
import time

f = open("sus.txt", "r", encoding = "utf-8")
current_balance = f.readline().strip()
f.close()
input_balance = 0

print("Текущий баланс", current_balance)

choice = pyautogui.confirm(title = "Сбер", text = "Выберите действие", buttons = [ "+", "-" ])

if choice == "+":
    input_balance = int(input("Сколько добави30ть на баланс? "))
    current_balance = int(current_balance) + input_balance
    
    f = open("sus.txt", "w", encoding = "utf-8")
    f.write(str(current_balance))
    f.close

else:
    input_balance = int(input("Сколько снять? "))
    current_balance = int(current_balance) - input_balance
    f = open("sus.txt", "w", encoding = "utf-8")
    f.write(str(current_balance))
    f.close

f = open("sus.txt", "r", encoding = "utf-8")
current_balance = f.readline().strip()
f.close()

print("Ваш текущий баланс", current_balance)