z=input("Куда записать идею? (1-идеи 2-задачи 3-покупки) ")
txt=input("Введитье запись . . . ")
if z == "1":
    f = open('id.txt', 'a', encoding="utf-8")
    f.write("\n"+"- "+txt)
    f.close()
elif z == "2":
    f = open('zd.txt', 'a', encoding="utf-8")
    f.write("\n"+"- "+txt)
    f.close()
elif z == "3":
    f = open('pk.txt', 'a', encoding="utf-8")
    f.write("\n"+"- "+txt)
    f.close()
else:
    print("Хихи ХАХА НЕСХОХРОНИЛОСЬ")