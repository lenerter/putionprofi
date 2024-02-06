n1=int(input("1 число-"))
n2=int(input("2 число-"))
n3=int(input("3 число-"))
if n3 == 0:
    n3=1

if n3 > 0:
    if n1 > n2:
        print("Ошибка 404")
    else:
        pass
elif n3 < 0:
    if n1 < n2:
        print("Ошибка 202")
    else:
        pass

for i in range(n1, n2, n3):
    print(i)