f = open('inp.txt', 'r', encoding="utf-8")
shopping_list = f.readlines()
formatted_list = []
for item in shopping_list:
    item = item.rstrip('\n')
    formatted_item = '- ' + item + '.'
    formatted_list.append(formatted_item)
f.close()
f = open('out.txt', 'w', encoding="utf-8")
f.write('\n'.join(formatted_list))
f.close()