"""
Вася написал программу, которая получает, сколько есть киселя
в ложках. На 1 ложку нужно добавлять половину литра воды.
Но когда Вася ввёл, что у него две с половиной ложки киселя,
программа почему-то выдала ошибку. Как это исправить?
"""

lojki = float(input("Введите количество ложек: "))
litryVody = lojki * 0.5
print("Нужно добавить", litryVody, "литров воды")