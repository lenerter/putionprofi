import random

print("УГАДАЙКА 2000 запушена")
print("-----------------------------------")
maxkolvo=int(input("Макс. число в угадайке_"))

if maxkolvo < 0:
    maxkolvo*=(-1)

secretnum=random.randint(0,maxkolvo)

print("ЧИСЛО гненерируется")
print("================================")
print("ЧИСЛО сгенерировано")

playernum=int(input("Ваши догатки?"))

if playernum == secretnum:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Вы победили")
    print("ВАШ ОТВЕТ_"+str(playernum))
else:
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Вы проиграли")
    print("ПРАВИЛЬНЫЙ ОТВЕТ_"+str(secretnum))