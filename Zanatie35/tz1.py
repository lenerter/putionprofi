sp = ["a", "b", "c", "d", "e", "h","g", "i"]
x=0
for x in range(8):
    sp[x]=input("Введите слово ")
print(sp)

if "молоко" in sp:
    print("Есть молоко")
else:
    print("Нет молока")