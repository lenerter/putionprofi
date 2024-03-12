sp=[]
zd=0
while zd != "stop":
    zd=input("Введите команду-")
    if zd == "add":
        sp.append(input("Что добавить?-")) 
    elif zd == "rem":
        sp.remove(input("Что удалить?-")) 
    elif zd == "prt":
        print(zd)
    else:
        pass