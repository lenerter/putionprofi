f = open('zag.txt', 'r', encoding="utf-8")
otv = f.readlines()
f.close()
securiti="0"
print("Абобус по другому?")
print("фортинайт или бабаджи?")
print("ТОП ИГРА В МИРЕ?")
print("маоя жизнь это?")
pr=input("Введите ответ на одну из загадок ")
if pr == "отгадано":
    print("АХ ТЫ ГЛУПИЙ ЧИТЕР БАН !!!")
else:
    securiti="1"
    gm=pr

if securiti == "1":
    f = open('zag.txt', 'w', encoding="utf-8")
    if gm == "автобус":
        f.write("отгадано"+"\n"+otv[1]+otv[2]+otv[3])
        f.close()
        print("Ура вы отгадали")
    elif gm == "фортнайт" :
        f.write(otv[0]+"отгадано"+"\n"+otv[2]+otv[3])
        f.close()
        print("Ура вы отгадали")
    elif gm == "кодм":
        f.write(otv[0]+otv[1]+"отгадано"+"\n"+otv[3])
        f.close()
        print("Ура вы отгадали")
    elif gm == "маинкрафт":
        f.write(otv[0]+otv[1]+otv[2]+"\n"+"отгадано")
        f.close()
        print("Ура вы отгадали")
    else:
        print("Такого ответа нет")
        f.write(otv[0]+otv[1]+otv[2]+otv[3])
        f.close()
else:
    print(";;;;;; you was banned form admin - suser235 ;;;;;;")

