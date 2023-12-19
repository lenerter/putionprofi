x=0
f = open('kto.txt', 'r', encoding="utf-8")
kto_list = f.readlines()
f.close()
f = open('zto.txt', 'r', encoding="utf-8")
zto_list = f.readlines()
f.close()
zto_ogg=[]
for item in zto_list:
    item = item.rstrip('\n')
    formatted_item = str(item)
    zto_ogg.append(formatted_item)

hoo_gotovo = []
for item in kto_list:
    item = item.rstrip('\n')
    formatted_item = str(item) +str(zto_ogg[x])
    hoo_gotovo.append(formatted_item)
    x+=1
f = open('gotovo.txt', 'w', encoding="utf-8")
f.write('\n'.join(hoo_gotovo))
f.close()
