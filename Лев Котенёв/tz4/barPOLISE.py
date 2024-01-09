nf = input("Напишите ваше имя и фамилию через пробел _______ ___ (НА РУССКОМ!!!)")

f = open('baned.txt', 'r', encoding="utf-8")
baned = f.readlines()

if nf == baned[0]:
    print("Вход воспрещён!!!")
    f.close()
elif nf == baned[1]:
    print("Вход воспрещён!!!")
    f.close()
elif nf == baned[2]:
    print("Вход воспрещён!!!")
    f.close()
else:
    time=input("Какое сейчас время? __:__ ")
    f.close()
    f = open('spiSOK.txt', 'a', encoding="utf-8")
    f.write("\n"+nf+" "+time)
    f.close()
    print("Добро пожаловать "+nf)