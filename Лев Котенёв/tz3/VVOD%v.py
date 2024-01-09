war=input("Введи + если хочеш дополнить или = если хочеш увидеть всю записаную информацию. ")

f = open('==listOFv==.txt', 'r', encoding="utf-8")
textR = f.readlines()
    
if war == "+":    
    date=input("Дата ____-__-__ ")
    time=input("Время __:__ ")
    vloz=input("Влажность __ ")
    NewTXT = "\n" + date + " " + time + " " + vloz
    f.close()
    f = open('==listOFv==.txt', 'a', encoding="utf-8")
    f.write(NewTXT)
elif war == "=":
    print(textR)
else:
    print("error 404")
f.close()