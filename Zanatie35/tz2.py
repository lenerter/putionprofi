sp=["a", "b", "c", "d","e"]
i=0
x=0
for i in range(5):
    print(sp[i])
    v=input("Что зделать? ")
    if v == "del":
        sp[i]="deliteONLY"
        x+=1
    elif v == "zam":
        sp[i] = input("На что? ")
    elif v == "ost":
        sp[i]=sp[i]
for i in range(x):
    sp.remove("deliteONLY")
print(sp)    