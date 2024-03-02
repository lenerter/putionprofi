import shutil
f = open('1.txt', 'r', encoding="utf-8")
f1 = f.readlines()
print("Название 1 cодержание "+str(f1))
a=input("Переместить в важное yes|no ")
if a == "yes":
    shutil.copy("1.txt","vazno/1.txt")
if a == "no":
    pass
f.close()

f = open('2.txt', 'r', encoding="utf-8")
f1 = f.readlines()
print("Название 2 cодержание "+str(f1))
a=input("Переместить в важное yes|no ")
if a == "yes":
    shutil.copy("2.txt","vazno/2.txt")
if a == "no":
    pass
f.close()    