f = open('sravn.txt', 'r', encoding="utf-8")
textR = f.readlines()
if textR[0] >= textR[1]:
    bol=textR[0]
elif textR[1] >= textR[0]:
    bol=textR[1]
elif textR[0] == textR[1]:
    bol="Ошибка они равны"
f.close()    
f = open('sravn.txt', 'a', encoding="utf-8")
f.write("Большее из этих двух чисел — "+bol)
f.close()