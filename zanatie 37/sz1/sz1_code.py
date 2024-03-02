spk=["sas","sus","ses","cyc","abeba"]
print("Эл жур \n--список-- \n1-sas \n2-sus \n3-ses \n4-cyc \n5-abeba")
while True:
    print("Оценки сейчас "+str(spk))
    y=input("Введите номнр ученика которому ставить оценку-")
    o=input("Введите оценку-")
    spk[int(y)-1]=spk[int(y)-1]+","+str(o)
    print("Готово")
    print("---------------")

