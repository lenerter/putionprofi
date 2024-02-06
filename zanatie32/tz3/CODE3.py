num=int(input("Введите число-"))
num = num + 1
x=0
for i in range(1, num, 1):
    f = open('sl.txt', 'a', encoding="utf-8")
    f.write("\n"+str(i))
    x+=i
    f.close()
f = open('sl.txt', 'a', encoding="utf-8")
f.write("\n"+str(x))
f.close()
    